# Unofficial snap for Mastodon 4.2.7

⚠️ This release is an important security release fixing a major security issue in Mastodon.

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.2.7

This release contains:

* Mastodon 4.2.7
* Node 16.20.2 (see [#25787](https://github.com/mastodon/mastodon/discussions/25787#discussioncomment-6382898))
* Ruby 3.2.3
* Bundle 2.4.13
* Yarn 1.22.21
* Nginx 1.25.4
* PostgreSQL 16.2
* Redis 7.2.4
* Acme.sh 3.0.7
* ImageMagick 7.1.1-28
* OpenSSL 1.1.1w
* Curl 8.6.0
* Jemalloc 5.3.0
* musl-libc 1.2.4
* mastodon-bird-ui 1.8.4
* tangerine-ui 1.9.4

Changelog:

* Uploaded media are excluded from pre-update backups.
* The creation of pre-update backups can be disabled using the `update.backups` setting.
* Only the last three pre-update backups are kept.
