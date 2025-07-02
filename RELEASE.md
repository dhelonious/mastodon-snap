# Unofficial Snap for Mastodon 4.3.9

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.9

This release also includes:

* ffmpeg 7.1.1
* libvips 8.17.0
* nginx 1.29.0
* node 20.19.3
* postgres 17.5
* redis 8.0.2
* ruby 3.3.5

Changelog for 4.3.9snap1:

* Update libvips to 8.17.0
* Update nginx to 1.29.0
* Update node to 20.19.3

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf` (versions >= 4.3.5snap1).
