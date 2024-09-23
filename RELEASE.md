# Unofficial snap for Mastodon 4.3.0-beta.2

⚠️ Requires rebuilding Elasticsearch accounts index: `mastodon-server.tootctl search deploy --only=accounts`
⚠️ StatsD integration has been removed, replaced by OpenTelemetry integration
ℹ️ The logging format of the streaming server has changed

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.0-beta.2

This release also includes:

* node 20.17.0
* ruby 3.3.5
* nginx 1.27.1
* postgres 16.4
* redis 7.4.0
* libvips 8.15.3
* ffmpeg 7.0.2

Changelog for 4.3.0-beta.2snap2:

* Upgrade to core24
* Adds `cleanup.headers` and `cleanup.accounts` settings
* Reduces default value of `cleanup.days` to 3
* Removes openssl1
* Removes explicit builds for lib-musl, jemalloc, curl
* Adds explicit builds for libvips and ffmpeg
* Uses non-root user for nginx, acme.sh, redis and Mastodon (backend, streaming, sidekiq)
* Adds redis database to exports
* Adds `db-migrate`, `db-rollback` and `maintenance` commands
* Renames `mastodon-server.postgres-dump` to `mastodon-server.db-dump`, which uses `pg_dump` instead of `pg_dumpall`
