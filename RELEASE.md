# Unofficial snap for Mastodon 4.3.7

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.7

This release also includes:

* ffmpeg 7.1.1
* libvips 8.16.1
* nginx 1.28.0
* node 20.19.1
* postgres 17.4
* redis 7.4.3
* ruby 3.3.5

Changelog for 4.3.7snap4:

* Update `yarn` to 4.9.1
* Update `node` to 20.19.1
* Update `nginx` to 1.28.0
* Update `redis` to 7.4.3
* Update `acme.sh` to 3.1.1

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf` (versions >= 4.3.5snap1).
