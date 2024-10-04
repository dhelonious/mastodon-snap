Unofficial snap for Mastodon 🦣📦


# 📌 About

The [Fediverse](https://en.wikipedia.org/wiki/Fediverse) is intended to remove the dependency on a single service provider. But users are still dependent on the instance providers. While a user can register with multiple instances and switch between them, their data is still tied to one instance at a time. In addition, users still do not have full control over their own data.

So anyone should be able to host their own Mastodon instance on a home server, an old PC, a VPS or even a RasPi. However, creating a Mastodon instance requires some advanced knowledge and skills. The officially provided [Docker Compose file](https://github.com/mastodon/mastodon/blob/main/docker-compose.yml) reduces the complexity by a good amount. However, some knowledge of Docker and some occasional debugging is still required.

The goal of this project is to further simplify the installation process of Mastodon to give everyone the ability to host their own fully functional (micro) instance of Mastodon without requiring any prior knowledge of the technology behind it. This all-in-one snap package also includes a database and support for ACME to automatically obtain SSL certificates for HTTPS. Because snaps are self-updating, the process of setting up a Mastodon instance can be reduced to the execution of a single command, with a minimum of future maintenance required.

Supported architectures:

* amd64

For more information, see the latest [release readme](RELEASE.md).


# 🚀 Quickstart

    sudo snap install mastodon-server

    sudo mastodon-server.setup
    sudo mastodon-server.get-certificate

    mastodon-server.tootctl accounts create administrator --email admin@example.com --role Owner --confirmed

Congratulations! You are now the owner of your very own Mastodon instance!


# 📦 Installation

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/mastodon-server)

If you prefer, you can also install the snap directly from the command line:

    sudo snap install mastodon-server

A common criticism of snaps is their dependence on Canonical. However, it is possible to install snaps offline and also build them directly from source.

## Install from a snap file

Download a snap file of the desired `VERSION` (e.g. `4.2.4snap1`) and `ARCH` (e.g. `amd64`). It can be installed using:

    sudo snap install mastodon-server_VERSION_ARCH.snap --dangerous

> Note: In this context *dangerous* means that the local snap file is unsigned.

## Build the snap file

It is also possible to build the snap file yourself:

1. Clone this repository:

    git clone https://github.com/dhelonious/mastodon-server

2. Build the snap by running

    snapcraft

in the repository's root directory.

> Note: Snapcraft relies on either `multipassd` or `lxd` to create snaps inside a virtual machine. Therefore, snaps cannot be created on a virtual infrastructure that does not support nested virtualization.

## Updates

A Snap Store installation is automatically updated when new versions are released.

To update your local installation, you can simply repeat the steps above with a newer version of the snap file. This will update your Mastodon instance in-place by creating a new snap revision.

If you have installed a snap file locally and still want to benefit from automatic updates, you can switch to the Snap Store installation using:

    snap refresh --amend mastodon-server

After the snap has updated itself, a new unpublished announcement will be created. You can review, publish or delete these announcements in *Preferences/Administration/Announcements*.

> Note: Be aware that there will always be a short downtime due to the way snaps are updated.


# 🦣 Setup your instance

An initial setup command is required to initialize the database and configuration files for Mastodon:

    sudo mastodon-server.setup

> Note: Be patient if you have changed the `status.char-limit` or `status.char-counter`, as it takes some time to recompile the assets. Ideally, these values should be changed before setup.

## Create admin user

Once the snap is set up, an administrator account with a randomly generated password can be created using the `tootctl` command:

    sudo mastodon-server.tootctl accounts create administrator --email admin@example.com --role Owner --confirmed

> Note: Be patient, the creation of an account takes some time.

## SSL

SSL certificates can be obtained via ACME from either [Let's Encrypt](https://letsencrypt.org/) or [ZeroSSL](https://zerossl.com/) (see the `acme.server` setting below):

    mastodon-server.get-certificate

> Note: `get-certificate` will automatically enable HTTPS on port `ports.https`.

> Note: HTTP is no longer supported in production. Mastodon will always serve https:// links.

If you want to provide your own certificates, you will need to place the private key and full chain certificate in the following locations:

* `/var/snap/mastodon-server/common/certs/<domain>_ecc/<domain>.key`
* `/var/snap/mastodon-server/common/certs/<domain>_ecc/fullchain.cer`

Restart the `nginx` service afterwards:

    snap restart mastodon-server.nginx


# ⚙️ Configuration

Basic settings can be configured using key-value pairs:

    sudo snap set mastodon-server KEY=VALUE

The following settings are available:

| Key                   | Values                        | Default value          | Description                                                                          |
|-----------------------|-------------------------------|------------------------|--------------------------------------------------------------------------------------|
| `domain`              | valid FQDN                    |                        | FQDN of the Mastodon instance                                                        |
| `email`               | valid e-mail                  |                        | E-mail address of the owner of the Mastodon instance                                 |
| `ports.http`          | 0 to 65353                    | 80                     | HTTP port                                                                            |
| `ports.https`         | 0 to 65353                    | 443                    | HTTPS port                                                                           |
| `acme.server`         | letsencrypt, zerossl          | letsencrypt            | CA used for acquiring an SSL certificate                                             |
| `update.backups`      | true, false                   | true                   | Create a backup in `/var/snap/mastodon-server/common/update/backups` before updating |
| `status.char-limit`   | integer                       | 500                    | Character limit of statuses (toots); changes require recompilation of assets, which takes some time [1] |
| `status.char-counter` | integer                       | 500                    | Character counter shown for statuses (toots); changes require recompilation of assets, which takes some time [1] |
| `media.dir`           | absolute path                 | `$SNAP_COMMON/media`   | Location of the media directory (*public/system*)                                    |
| `backup.dir`          | absolute path                 | `$SNAP_COMMON/backups` | Location of the backup directory                                                     |
| `backup.days`         | integer                       | 0                      | Create and keep backups for `backup.days` (enabled if > 0)                           |
| `cleanup.days`        | integer                       | 3                      | Cleanup media and statuses older than `cleanup.days` (enabled if > 0)                |
| `cleanup.media`       | true, false                   | true                   | Cleanup media files, see [tootctl media remove](https://docs.joinmastodon.org/admin/tootctl/#media-remove) |
| `cleanup.headers`     | true, false                   | true                   | Cleanup headers, see [tootctl media remove](https://docs.joinmastodon.org/admin/tootctl/#media-remove) |
| `cleanup.previews`    | true, false                   | true                   | Cleanup preview cards, see [tootctl preview_cards remove](https://docs.joinmastodon.org/admin/tootctl/#preview_cards) |
| `cleanup.statuses`    | true, false                   | true                   | Cleanup unreferenced statuses, see [tootctl statuses remove](https://docs.joinmastodon.org/admin/tootctl/#statuses-remove) |
| `cleanup.orphans`     | true, false                   | false                  | Cleanup orphaned media files, see [tootctl media remove-orphans](https://docs.joinmastodon.org/admin/tootctl/#media-remove-orphans) |
| `cleanup.accounts`    | true, false                   | false                  | Cleanup user accounts, see [tootctl accounts delete](https://docs.joinmastodon.org/admin/tootctl/#accounts-delete) |
| `log.access.enabled`  | true, false                   | false                  | Logging of http(s) accesses                                                          |
| `log.access.format`   | standard, anonymized, privacy | anonymized             | Use of real/anonymized/no IP addresses in the access log                             |

[1] Setting this value will increase the time it takes for snapcraft to update this snap. This will increase the downtime of your instance.

You can also set multiple values at once using

    sudo snap set mastodon-server KEY1=VALUE1 KEY2=VALUE2

> Note: This is particularly useful if you want to change both `status.char-limit` and `status.char-counter`, as the assets only need to be recompiled once.

Configuration files can be used for further customization.

## Single user instances

If you plan to use your instance for yourself only, you may want to enable `SINGLE_USER_MODE` in `/var/snap/mastodon-server/common/mastodon.conf`. This will disable registrations on your instance. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#single_user_mode) for more information.

## Data privacy

By default, this snap will not log accesses unless `log.access.enabled` is `true`. Otherwise, the IP addresses in the access logs are anonymized by removing the last octet of each IP address (e.g. 192.168.100.10 becomes 192.168.100.0). If you want to change this, for example for debugging or to use [fail2ban](https://github.com/fail2ban/fail2ban), you can set `log.access.format` to `standard`.

> Note that even if access logging is enabled and not anonymized, the log files are rotated daily and anonymized.

Also, to allow Mastodon to store IP addresses, you need to increase the value (in seconds) of `IP_RETENTION_PERIOD` in `/var/snap/mastodon-server/common/mastodon.conf`. For example, to set the retention period to 24 hours, use:

    IP_RETENTION_PERIOD=86400

You may also be interested in enabling what is also known as *secure mode* via `AUTHORIZED_FETCH`. This setting prevents unauthenticated access to your instances at the cost of some computational overhead. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#authorized_fetch) for more details.

## Mail

Add the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    SMTP_SERVER=smtp.example.com
    SMTP_PORT=465
    SMTP_LOGIN=mastodon@example.com
    SMTP_PASSWORD=********
    SMTP_AUTH_METHOD=plain
    SMTP_SSL=true
    SMTP_OPENSSL_VERIFY_MODE=none
    SMTP_ENABLE_STARTTLS=always
    SMTP_FROM_ADDRESS="Mastodon <mastodon@example.com>"

## Elasticsearch

Elasticsearch provides some advanced search features and is required for the posts to be searchable at all. Due to its size, Elasticsearch is not included in this snap. An [external installation](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html) can be used by adding the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    ES_ENABLED=true
    ES_HOST=localhost
    ES_PORT=9200
    ES_PRESET=single_node_cluster
    ES_USER=elastic
    ES_PASS=********

> Note: `ES_USER` and `ES_PASS` are required if `xpack.security` is enabled in `/etc/elasticsearch/elasticsearch.yml` (see [docs.joinmastodon.org/admin/elasticsearch](https://docs.joinmastodon.org/admin/elasticsearch/#security) for details).

Create the elasticsearch indexes using the following command:

    mastodon-server.tootctl search deploy

## S3 Storage

Add the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    S3_ENABLED=true
    S3_FORCE_SINGLE_REQUEST=true
    S3_HOSTNAME=s3.example.com
    S3_ENDPOINT=https://s3.example.com
    S3_BUCKET=mastodon
    AWS_ACCESS_KEY_ID=********
    AWS_SECRET_ACCESS_KEY=********

> Note: `S3_FORCE_SINGLE_REQUEST` allows Mastodon to handle large uploads properly. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#s3) for a full list of options.

The [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) must allow for objects to be publicly readable. This is an example of a minimal policy that works:

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Principal": {
            "AWS": "*"
          },
          "Effect": "Allow",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::mastodon-server/*"
        }
      ]
    }

## Translation backend

Since version 4.0 Mastodon can use [DeepL](https://www.deepl.com) and [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) to translate toots automatically.

The following configuration variables can be used in `/var/snap/mastodon-server/common/mastodon.conf` to enable the backend:

* DeepL: [`deepl_api_key`](https://docs.joinmastodon.org/admin/config/#deepl_api_key) and [`deepl_plan`](https://docs.joinmastodon.org/admin/config/#deepl_plan)
* LibreTranslate: [`libre_translate_endpoint`](https://docs.joinmastodon.org/admin/config/#libre_translate_endpoint) and [`libre_translate_api_key`](https://docs.joinmastodon.org/admin/config/#libre_translate_api_key)

> Note that LibreTranslate is not included in this snap due to its size.

## Reverse proxy

Mastodon snap can also be used behind a reverse proxy along with other web services. In this case, SSL must not be enabled because SSL termination is done at the reverse proxy. Also, `ports.http` should be changed from the default (e.g. to `ports.http=81`).

Here is a sample configuration for an nginx reverse proxy:

    upstream mastodon {
        zone upstreams 64K;
        server 127.0.0.1:81 max_fails=1 fail_timeout=2s;
        keepalive 2;
    }

    server {
        listen 80;
        server_name example.com;
        access_log /var/log/nginx/example.com.access.log;
        error_log /var/log/nginx/example.com.error.log;

        location /.well-known/ {
            proxy_pass http://mastodon/.well-known/;
        }

        return 301 https://social.dhelonious.de;
    }

    server {
        listen 443 ssl;
        server_name example.com;
        access_log /var/log/nginx/example.com.access.log;
        error_log /var/log/nginx/example.com.error.log;

        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf;
        ssl_dhparam /etc/ssl/certs/dhparam.pem;

        add_header Strict-Transport-Security "max-age=15768000; includeSubDomains" always;
        add_header Front-End-Https on;

        client_max_body_size 0;

        location / {
            proxy_pass http://mastodon/;

            proxy_http_version 1.1;
            proxy_pass_header Server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Content-Type-Options "nosniff";
            proxy_set_header X-Robots-Tag "noindex,nofollow";
            proxy_set_header X-Frame-Options "SAMEORIGIN";
            proxy_set_header X-XSS-Protection "1; mode=block";
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
        }
    }


# 🛠️ Usage

## Themes

Coming from ~~Twitter~~ X and wanting a familiar look? Then the included [Mastodon Bird UI](https://github.com/ronilaukkarinen/mastodon-bird-ui) and [Tangerine UI](https://github.com/nileane/TangerineUI-for-Mastodon) themes might be for you. While *Mastodon Bird UI* retains the separation between dark, light and high contrast variants, *Tangerine UI* automatically switches to a light or dark variant depending on what your browser requests. You can change the theme in *Preferences/Appearance*.

> Important: If you have a severe visual impairment, an [accessible version of the Bird UI theme](https://github.com/ronilaukkarinen/mastodon-bird-ui#how-to-install-an-accessible-version-built-for-people-with-serious-vision-impairment) is included by default. This theme is indicated by the phrase ***High contrast++***, which contains ***two plus signs*** and is translated into your selected language. In addition, this theme is marked with the ♿ ***emoji representing a person in a wheelchair*** as the [International Symbol of Access](https://en.wikipedia.org/wiki/International_Symbol_of_Access).

## Database shell

To access the postgres database shell, use:

    sudo mastodon-server.psql

> Tip: Use `\pset pager on` and `\setenv PAGER 'less -S'` to prevent line wrapping.

## Rails console

To access the rails console, use:

    sudo mastodon-server.console

## Export

To export the database and the configuration file into `/var/snap/mastodon-server/common/backups/%Y%m%d-%H%M%S/`, use:

    sudo mastodon-server.export

Note that exports do not include media cached from other servers. This means that media attachments in feeds received prior to export will be missing. This includes media attachments in boosted or favoured posts. However, missing media will be downloaded if you use the restore command described below.

> If you just want to export the Mastodon database, use the `db-dump` command.

> The backup dir can be changed using the `backup.dir` setting. If backups are to be stored on external storage the snap must be connected to the `removable-media` plug.

## Restore

A backup can be restored using the `mastodon-server.restore` command, e. g:

    sudo mastodon-server.restore 20230201-010203

> Note: This command has bash completion if your shell supports it.

> Note: The error messages indicating that some roles already exist can be safely ignored.

If the media cache is lost between export and restore, the [tootctl media refresh command](https://docs.joinmastodon.org/admin/tootctl/#media-refresh) can be used with `--force` to manually restore media files. In general, `--account` is used to restore media attachments from a specific external user. Experts can also use `--status` and restore specific images after retrieving their IDs from the database. Using `--days` a larger amount of media can be restored.

> Note: Changes to `mastodon.conf` may be required when restoring from an older version. Check the changelog and compare the configuration files.

## Cleanup media and statuses

Media and statuses are cleaned up nightly. You can control how long media is kept by changing the value of `cleanup.days`:

    sudo snap set mastodon-server cleanup.days=7

You can further control which content to clean up by using the `cleanup.media`, `cleanup.previews`, `cleanup.statuses` and `cleanup.orphans` settings.

> Note: Depending on the activity on your server, the amount of storage required for media can be significant. Reducing the number of days media is kept should help in this case.

## Generate secrets

If you want to change the `SECRET_KEY_BASE` or your `OTP_SECRET`, you can use the following command:

    mastodon-server.generate-secret

A vapid key can be generated using:

    mastodon-server.generate-vapid-key

The database encryption keys can be generated using:

    mastodon-server.generate-db-encryption-keys

## External media storage

The media directory can grow quickly, depending on how busy your server is. To move the media directory to an external volume mounted under `/media` or `/mnt`, you must first allow snap access to external media:

    sudo snap connect mastodon-server:removable-media

If the default media dir `/var/snap/mastodon-server/common/media` already contains files, you can transfer them to your external directory:

    sudo rsync -a /var/snap/mastodon-server/common/media /media/mastodon

Change the `media.dir` settings to your external directory:

    sudo set mastodon-server media.dir=/media/mastodon

You can then remove the old media directory.


# 🔥 Troubleshooting

If none of the answers below help you, you can always re-install the snap and restore a backup:

    snap remove mastodon-server
    snap install mastodon-server
    mastodon-server.restore 20240312-123456

Make sure you move the backups out of `/var/snap/mastodon-server/common/backups/` before removing the snap.

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

If you are unable to solve the problem, or the problem cannot be solved due to the read-only file system of the snap, try the `snap revert` command to revert to the previous revision.

If reverting does not work or is not possible, try `snap remove` and reinstall the snap. You should also make a backup of the media in `/var/snap/mastodon-server/common/media/` if you have not already done so using `mastodon-server.export`. After installation, the postgres database should be initialized and working. Stop the snap with `snap stop mastodon-server` and replace the data dir, password file and media dir with your backups and change the permissions and ownership of the postgres data dir:

    chown -R snap_daemon:root /var/snap/mastodon-server/current/postgres/data/
    find /var/snap/mastodon-server/current/postgres/data/ -type f -exec chmod 600 {} \;
    find /var/snap/mastodon-server/current/postgres/data/ -type d -exec chmod 700 {} \;

Then change the permissions of the password file:

    chmod 640 /var/snap/mastodon-server/common/secrets/postgres

Use `snap start` to restart the snap. Wait for postgres to start and use the `mastodon-server.export` command to create a proper backup. If postgres still does not work, repeat the above steps with a previous version of snap (e.g. if your postgres data dir was created by an older major version of postgres).

> Note: This procedure requires root privileges.

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

## 2FA issues

### I cannot enable 2FA due to an ArgumentError: key must be 32 bytes or longer

Generate a new `OTP_SECRET` using `mastodon-server.generate-secret`. Alternatively, you can use the rails console:

    mastodon-server.console
    User.generate_otp_secret(32)

It may also be necessary to clean up the `encrypted_otp_secret` in the Mastodon database. To do this, log in to the `mastodon` database:

    mastodon-server.psql
    \c mastodon

Find user `id`:

    select id from users where email='me@example.com';

For example, if your user `id` is `1`, you can delete the `encrypted_otp_secret` as follows:

    update users set encrypted_otp_secret = null where id=1;

## Profile link verification not working

If you try to [verify a profile link](https://docs.joinmastodon.org/user/profile/#verification) to a website that is running on the same server as your instance, the hostname will probably point to your internal IP address. However, for security reasons, Mastodon denies access to private IP addresses (see [#10361](https://github.com/mastodon/mastodon/issues/10361#issuecomment-678610290)).

To allow Mastodon to access your private server IP, you can add it to the `ALLOWED_PRIVATE_ADDRESSES` variable in `/var/snap/mastodon-server/common/mastodon.conf`. This variable contains a comma-separated list of allowed IP addresses and subnets in outgoing HTTP requests.


# 🔗 Resources

- [Fedi.Tips](https://fedi.tips/) is a valuable resource for Mastodon and the Fediverse.
- [Fedi.Directory](https://fedi.directory/) can help you find interesting accounts to follow.
- [FediDB](https://fedidb.org/) provides statistics on the Fediverse.
- [FediBuzz Relay](https://relay.fedi.buzz/) can be used to follow hashtags on other instances.


# 📋 TODO

- [ ] Test on arm64
- [ ] Use GitHub-hosted arm64 runner when available (https://github.com/orgs/community/discussions/19197)
- [ ] Submit to Snapcrafters (see https://github.com/snapcrafters/fork-and-rename-me)
