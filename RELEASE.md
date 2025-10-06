# Unofficial Snap for Mastodon 4.4.5

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.4.5

This release also includes:

* ffmpeg 8.0
* libvips 8.17.2
* nginx 1.29.1
* node 20.19.5
* postgres 17.6
* redis 8.2.2
* ruby 3.4.4

Changelog for 4.4.5snap2:

* Update redis to 8.2.2
* Remove the `update.backup` feature, since it is generally not required. If the refresh fails, the snapshot reverts to the previous version without any loss of data.
* Add debug logging
* Rework the database upgrade procedure so that it uses `pg_upgrade`
