# Unofficial Snap for Mastodon 4.5.4

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.5.4

This release also includes:

* ffmpeg 8.0.1
* libvips 8.18.0
* nginx 1.29.4
* node 20.20.0
* pgbouncer 1.25.1
* postgres 18.1
* redis 8.4.0
* ruby 3.4.7

> [!IMPORTANT]
> Release 4.5.4snap1 should have greatly enhanced performance due to the addition of pgbouncer, extra sidekiq workers, and support for tuning based on system hardware. Take a look at the tuning section of the [readme](README.md) to find out more.

Changelog for 4.5.4snap2:

* Add an additional `-p` option to the `mastodon-server.export` and `mastodon-server.restore` commands to select the path (requires the connection of the `removable-media` interface, see [docs/configuration.md](docs/configuration.md)).
* Add the ability to specify a directory name in `mastodon-server.export`.
