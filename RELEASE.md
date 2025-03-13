# Unofficial snap for Mastodon 4.3.6

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.6

This release also includes:

* ffmpeg 7.1.1
* libvips 8.16.1
* nginx 1.27.4
* node 20.19.0
* postgres 17.4
* redis 7.4.2
* ruby 3.3.5

Changelog for 4.3.6snap1:

* Update `libvips` to 8.16.1
* Update `node` to 20.19.0

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf` (versions >= 4.3.5snap1).
