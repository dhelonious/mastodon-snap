# Unofficial snap for Mastodon 4.2.X

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.2.X

This release contains:

* Mastodon 4.2.X
* Node 16.20.2 (see [#25787](https://github.com/mastodon/mastodon/discussions/25787#discussioncomment-6382898))
* Ruby 3.2.3
* Bundle 2.4.13
* Yarn 1.22.22
* Nginx 1.25.4
* PostgreSQL 16.2
* Redis 7.2.4
* Acme.sh 3.0.7
* ImageMagick 7.1.1-29
* OpenSSL 1.1.1w
* Curl 8.6.0
* Jemalloc 5.3.0
* musl-libc 1.2.5
* mastodon-bird-ui 1.8.5
* tangerine-ui 1.9.4

⚠️ Previous versions of this snap set an incorrect path in the PostgreSQL configuration file. As a result, some settings may not be loaded after some updates. The snap will fix this when updated *after* this version. To fix this immediately, change the last line in `/var/snap/mastodon-server/current/postgres/data/postgres.conf` to `include_if_exists = '/var/snap/mastodon-server/current/postgres/config/postgresql.conf'` and restart the snap.
