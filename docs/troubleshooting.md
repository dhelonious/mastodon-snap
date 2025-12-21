# 🔥 Troubleshooting

To help with troubleshooting, a debug report containing an overview of the current installation's files, settings and variables can be generated:

    mastodon-server.debug-report

If none of the answers below help, you can always uninstall and reinstall the app and restore a backup:

    snap remove mastodon-server
    snap install mastodon-server
    mastodon-server.restore 20240312-123456

Before removing the Snap, make sure you move the backups out of `/var/snap/mastodon-server/common/backups/`.

> [!TIP]
> Additional debug logs will be created when the `log.debug` setting is enabled (see the [configuration docs](docs/configuration.md)).

## Statistics show "0 active users"

Statistics are compiled every night. So the number of users should be correct within 24 hours.

## Server admin info not loading

Go to *Preferences/Administration/Server settings/Branding* and add your *Contact username* and *Contact e-mail*.

## PgHero shows duplicate indexes

This can happen after updates. Use `mastodon-server.maintenance fix-duplicates` to fix corrupted database indexes. See also the [tootctl maintenance fix-duplicates] documentation (https://docs.joinmastodon.org/admin/tootctl/#maintenance-fix-duplicates).

## Requests fail after upgrade

If some requests fail after upgrading to a newer version, and there are log entries showing errors about missing columns and tables, the database has not been migrated properly. Use `mastodon-server.db-migrate` to start the migrations manually. Use `mastodon-server.db-rollback` to rollback the database migrations, which may be necessary when downgrading.

See the [Mastodon troubleshooting page](https://docs.joinmastodon.org/admin/troubleshooting/#after-an-upgrade-to-a-newer-version-some-requests-fail-and-the-logs-show-error-messages-about-missing-columns-or-tables-why) for more information.

## My postgres database has stopped working, how can I recover my data?

If your postgres database has stopped working, for example due to a failed upgrade, first backup the postgres data dir `/var/snap/mastodon-server/current/postgres/data/` and the password file `/var/snap/mastodon-server/common/secrets/postgres`.

Check the log file at `/var/snap/mastodon-server/current/logs/postgres/postgres.log`. The log message may contain instructions on how to fix the problem.

If you are unable to solve the problem, or the problem cannot be solved due to the read-only file system of the Snap, try the `snap revert` command to revert to the previous revision.

If reverting does not work or is not possible, try `snap remove` and reinstall the Snap. You should also make a backup of the media in `/var/snap/mastodon-server/common/media/` if you have not already done so using `mastodon-server.export`. After installation, the postgres database should be initialized and working. Stop the Snap with `snap stop mastodon-server` and replace the data dir, password file and media dir with your backups and change the permissions and ownership of the postgres data dir:

    chown -R snap_daemon:root /var/snap/mastodon-server/current/postgres/data/
    find /var/snap/mastodon-server/current/postgres/data/ -type f -exec chmod 600 {} \;
    find /var/snap/mastodon-server/current/postgres/data/ -type d -exec chmod 700 {} \;

Then change the permissions of the password file:

    chmod 640 /var/snap/mastodon-server/common/secrets/postgres

Use `snap start` to restart the Snap. Wait for postgres to start and use the `mastodon-server.export` command to create a proper backup. If postgres still does not work, repeat the above steps with a previous version of Snap (e.g. if your postgres data dir was created by an older major version of postgres).

> [!IMPORTANT]
> This procedure requires root privileges.

## Avatars/header images are missing for accounts I follow

Try re-downloading the images for this particular account:

    mastodon-server.tootctl accounts refresh <name@domain>

## The redis.log contains the following warning: Memory overcommit must be enabled

To fix this problem, add `vm.overcommit_memory = 1` to `/etc/sysctl.conf` and then reboot or run the command:

    sudo sysctl vm.overcommit_memory=1

## Backup issues

### "Too many open files" during restore

The message "Too many open files" indicates that you have reached the file descriptor limit. You can check the current limit with `ulimit -n`. You can try to increase the limit to its maximum using

    ulimit -n 65536

### Database export fails due to broken pages

    Export database
    pg_dump: error: Dumping the contents of table "statuses" failed: PQgetResult() failed.
    pg_dump: detail: Error message from server: ERROR:  invalid page in block 14781 of relation base/97120/97257
    pg_dump: detail: Command was: COPY public.statuses (id, uri, text, ...) TO stdout;
    pg_dumpall: error: pg_dump failed on database "mastodon", exiting

Find the table name in the error description. In this example, it is `public.statuses`. Then, run the following command to fix the broken pages:

    mastodon-server.psql

    postgres=# \c mastodon
    You are now connected to database "mastodon" as user "postgres".

    mastodon=# SET zero_damaged_pages = on;
    SET

    mastodon=# VACUUM FULL public.statuses;
    WARNING:  invalid page in block 14781 of relation base/97120/97257; zeroing out page
    VACUUM

    mastodon=# REINDEX TABLE public.statuses;
    REINDEX

## 2FA issues

### I cannot enable 2FA due to an ArgumentError: key must be 32 bytes or longer

Generate a new `OTP_SECRET` using `mastodon-server.generate-secret`. Alternatively, you can use the rails console:

    mastodon-server.console
    User.generate_otp_secret(32)

It may also be necessary to clean up the `encrypted_otp_secret` in the Mastodon database. To do this, log in to the `mastodon` database:

    mastodon-server.psql
    \c mastodon

Find user `id`:

    select id from users where email="me@example.com";

For example, if your user `id` is `1`, you can delete the `encrypted_otp_secret` as follows:

    update users set encrypted_otp_secret = null where id=1;

## Profile link verification not working

If you try to [verify a profile link](https://docs.joinmastodon.org/user/profile/#verification) to a website that is running on the same server as your instance, the hostname will probably point to your internal IP address. However, for security reasons, Mastodon denies access to private IP addresses (see [#10361](https://github.com/mastodon/mastodon/issues/10361#issuecomment-678610290)).

To allow Mastodon to access your private server IP, you can add it to the `ALLOWED_PRIVATE_ADDRESSES` variable in `/var/snap/mastodon-server/common/mastodon.conf`. This variable contains a comma-separated list of allowed IP addresses and subnets in outgoing HTTP requests.
