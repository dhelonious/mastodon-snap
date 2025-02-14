# 🚧 Maintenance

## Database shell

To access the postgres database shell, use:

    sudo mastodon-server.psql

> Tip: Use `\pset pager on` and `\setenv PAGER 'less -S'` to prevent line wrapping.

## Rails console

To access the rails console, use:

    sudo mastodon-server.console

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
