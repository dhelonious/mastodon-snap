# Unofficial Snap for Mastodon 4.3.9

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.9

This release also includes:

* ffmpeg 7.1.1
* libvips 8.17.1
* nginx 1.29.0
* node 20.19.3
* postgres 17.5
* redis 8.0.3
* ruby 3.3.5

Changelog for 4.3.9snap2:

* Update libvips to 8.17.1
* Update redis to 8.0.3

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf` (versions >= 4.3.5snap1).
