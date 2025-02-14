# 💾 Backups

## Export

To export the database and the configuration file into `/var/snap/mastodon-server/common/backups/%Y%m%d-%H%M%S/`, use:

    sudo mastodon-server.export

Note that exports do not include media cached from other servers. This means that media attachments in feeds received prior to export will be missing. This includes media attachments in boosted or favoured posts. However, missing media will be downloaded if you use the restore command described below.

> If you just want to export the Mastodon database, use the `db-dump` command.

> The backup dir can be changed using the `backup.dir` setting. If backups are to be stored on external storage the snap must be connected to the `removable-media` plug.

## Restore

A backup can be restored using the `mastodon-server.restore` command, e. g:

    sudo mastodon-server.restore 20230201-010203

If you wish to restore a backup to a fresh installation, you must first run the `mastodon-server.setup` command. The admin account created during setup will be replaced with the backed up account.

> Note: The error messages indicating that some roles already exist can be safely ignored.

If the media cache is lost between export and restore, the [tootctl media refresh command](https://docs.joinmastodon.org/admin/tootctl/#media-refresh) can be used with `--force` to manually restore media files. In general, `--account` is used to restore media attachments from a specific external user. Experts can also use `--status` and restore specific images after retrieving their IDs from the database. Using `--days` a larger amount of media can be restored.

> Note: Changes to `mastodon.conf` may be required when restoring from an older version. Check the changelog and compare the configuration files.

This command has bash completion if your shell supports it.

## Automatic backups

To enable automatic backups on a daily basis, you need to set the `backup.days` variable (see [configuration.md](configuration.md)).
