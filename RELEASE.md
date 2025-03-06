# Unofficial snap for Mastodon 4.3.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.3

This release also includes:

* ffmpeg 7.1.1
* libvips 8.16.0
* nginx 1.27.4
* node 20.18.3
* postgres 17.4
* redis 7.4.2
* ruby 3.3.5

Changelog for 4.3.4snap2:

* Add a server announcement 3 minutes before an update
* Add `mastodon-server.announce` command to create server announcements
* Rename `update.backups` to `update.backup
* Update `ffmpeg` to 7.1.1
* Update `yarn` to 4.7.0
* Improve output of interactive commands like `mastodon-server.setup`

⚠️ Post update instructions ⚠️

You should manually remove the entries corresponding to `Redis` and `PostgreSQL` from `/var/snap/mastodon-server/common/mastodon.conf`.
