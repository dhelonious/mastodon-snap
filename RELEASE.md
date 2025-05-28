# Unofficial Snap for Mastodon 4.3.8

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.8

This release also includes:

* ffmpeg 7.1.1
* libvips 8.16.1
* nginx 1.28.0
* node 20.19.2
* postgres 17.5
* redis 8.0.2
* ruby 3.3.5

Changelog for 4.3.8snap3:

* Update redis to 8.0.2

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf` (versions >= 4.3.5snap1).
