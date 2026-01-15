# 🧳 Migration

## Account migration

If you want to move your account to or from a public instance, you can simply [export and import](https://docs.joinmastodon.org/user/moving/#export) your account under *Preferences/Import and export*. You may then wish to [redirect or move your profile](https://docs.joinmastodon.org/user/moving/#migration) to your new instance.

> [!IMPORTANT]
> Mastodon currently does not support importing posts or media.

## Migrating an instance to the mastodon-server Snap

Requirements:

- A PostgreSQL database dump (created with `pg_dump`) or a cluster dump (created with `pg_dumpall`)
- A copy of the media directory (optional)

> [!TIP]
> To determine whether your database dump contains only one database or a cluster, use the following command:
>
>     head -n 1000 database.sql | grep 'Database ".*" dump'
>
> If you only see one line saying `Database "mastodon" dump`, then your database dump was created using `pg_dump mastodon`. Otherwise, the dump contains all databases and has been created using `pg_dumpall`.

First, install and set up a Mastodon Server Snap (see the [installation readme](README.md#-installation)). If your database dump only contains one database (mastodon), you can use the following commands to restore it:

    mastodon-server.psql -c "drop database if exists mastodon;"
    mastodon-server.psql < /path/to/database.sql

If the database dump was created using a lower version of Mastodon than the installed Snap, you must migrate the database using `mastodon-server.db-migrate`.

The media directory can be restored by copying the files to the Mastodon server's media directory. It is located by default in `/var/snap/mastodon-server/common/media`, but this can be changed to an external directory (see the [configuration docs](docs/configuration.md)). You can skip this part if you don't have a backup of your media directory.

Last but not least, you should always clean up and restore the media for recent posts:

    mastodon-server.tootctl preview_cards remove --days 1
    mastodon-server.tootctl media remove --days 1
    mastodon-server.tootctl media refresh --days 1 --force
    mastodon-server.tootctl accounts refresh --all --force

> [!NOTE]
> The `media refresh` and `accounts refresh` commands may take some time to complete depending on the number of posts in your database dump.

If you only have a PostgreSQL cluster dump, you can first use the `mastodon-server.export` command to create a new backup file (see the [backups guide](docs/backups.md) for more information). The backup directory will contain a database dump called `database.sql`. Delete and replace it with your file. If you have a backup of your media directory, archive it using the command

    tar -czf media.tar.gz /path/to/media

and place the archive in the export directory. Then run `mastodon-server.restore` to restore everything. This command will automatically handle database and media cleanup.

## Migrating an instance to a different Mastodon implementation

To migrate to a different Mastodon implementation (e.g. Docker or YunoHost), you can use the following command to create a database dump:

    mastodon-server.db-dump > database.sql

This file only contains the Mastodon database. Optionally, you can also save the contents of the media directory. Use `snap get mastodon-server media.dir` to find the location of the current media directory.

Providing detailed migration guides for all the different options is beyond the scope of this guide. Please refer to a specific migration guide for your chosen Mastodon implementation or, at the very least, learn how to restore a PostgreSQL dump.

[!TIP] You might also want to take a look at the official Mastodon documentation on [migrating to a new machine](https://docs.joinmastodon.org/admin/migrating/).
