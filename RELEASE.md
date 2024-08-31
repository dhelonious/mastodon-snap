# Unofficial snap for Mastodon 4.3.0-beta.1

⚠️ Requires rebuilding Elasticsearch accounts index: `mastodon-server.tootctl search deploy --only=accounts`
⚠️ StatsD integration has been removed, replaced by OpenTelemetry integration
ℹ️ The logging format of the streaming server has changed

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.0-beta.1

This release contains:

* mastodon 4.3.0-beta.1
* node 20.17.0
* ruby 3.3.4
* bundle 2.5.11
* yarn 4.4.1
* nginx 1.27.1
* postgres 16.4
* redis 7.4.0
* acme.sh 3.0.7
* logrotate 3.22.0
* libvips 8.15.3
* ffmpeg 7.0.2
* mastodon-bird-ui 2.0.0rc47
* tangerine-ui v2.0.0-prerelease6

Changelog for 4.3.0-beta.1snap1:

* Upgrade to core24
* Add `cleanup.headers` and `cleanup.accounts` settings
* Decrease default value of `cleanup.days` to 3
* Remove openssl1
* Remove explicit builds for lib-musl, jemalloc, curl
* Add explicit builds for libvips and ffmpeg
* Use non-root user for nginx, acme.sh, redis, and Mastodon (backend, streaming, sidekiq)
* Add redis database to exports

The result is a lighter and more secure snap file with a smaller file size.
