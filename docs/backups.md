# 💾 Backups

## Export

To export the database and the configuration file into `/var/snap/mastodon-server/common/backups/%Y%m%d-%H%M%S/`, use:

    sudo mastodon-server.export

Note that exports do not include media cached from other servers. This means that media attachments in feeds received prior to export will be missing. This includes media attachments in boosted or favoured posts. However, missing media will be downloaded if you use the restore command described below.

> [!NOTE]
> If you just want to export the Mastodon database, use the `db-dump` command.

> [!NOTE]
> The backup directory can be changed using the `backup.dir` setting (see the [configuration docs](docs/configuration.md)). If backups are to be stored on external storage, the Snap must be connected to the `removable-media` interface.

## Restore

A backup can be restored using the `mastodon-server.restore` command, e. g:

    sudo mastodon-server.restore 20230201-010203

This is also possible with a fresh installation that has not yet been set up. If required, a certificate must be created manually using `mastodon-server.get-certificate`.

> [!NOTE]
> The error messages indicating that some roles already exist can be safely ignored.

If the media cache is lost between export and restore, the [tootctl media refresh command](https://docs.joinmastodon.org/admin/tootctl/#media-refresh) can be used with `--force` to manually restore media files. In general, `--account` is used to restore media attachments from a specific external user. Experts can also use `--status` and restore specific images after retrieving their IDs from the database. Using `--days` a larger amount of media can be restored.

> [!IMPORTANT]
> Changes to `mastodon.conf` may be required when restoring from an older version. Check the changelog and compare the configuration files.

This command has bash completion if your shell supports it.

## Automatic backups

To enable automatic backups on a daily basis, you need to set the `backup.days` variable (see the [configuration docs](configuration.md)).
