# Unofficial snap for Mastodon 4.3.0-beta.1

❗ Requires new encryption secrets environment variables: `mastodon-server.db-encryption-init` and copy outputs to `/var/snap/mastodon-server/common/mastodon.conf`
⚠️ Requires rebuilding Elasticsearch accounts index: `mastodon-server.tootctl search deploy --only=accounts`
⚠️ StatsD integration has been removed, replaced by OpenTelemetry integration
ℹ️ The logging format of the streaming server has changed

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.0-beta.1

This release contains:

* Mastodon 4.3.0-beta.1
* Node 20.17.0
* Ruby 3.3.4
* Bundle 2.5.11
* Yarn 4.4.1
* Nginx 1.27.1
* PostgreSQL 16.4
* Redis 7.4.0
* Acme.sh 3.0.7
* OpenSSL 1.1.1w
* Curl 8.9.1
* Logrotate 3.22.0
* Jemalloc 5.3.0
* libvips 8.15.3
* musl-libc 1.2.5
* mastodon-bird-ui 2.0.0rc47
* tangerine-ui v2.0.0-prerelease6
