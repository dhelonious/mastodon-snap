# Unofficial Snap for Mastodon 4.5.6

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.5.6

This release also includes:

* ffmpeg 8.0.1
* libvips 8.18.0
* nginx 1.29.5
* node 20.20.0
* pgbouncer 1.25.1
* postgres 18.1
* redis 8.4.1
* ruby 3.4.7

> [!IMPORTANT]
> Release 4.5.4snap1 should have greatly enhanced performance due to the addition of pgbouncer, extra sidekiq workers, and support for tuning based on system hardware. Take a look at the tuning section of the [readme](README.md) to find out more.

Changelog for 4.5.6snap2:

* Update redis to 8.4.1
* Fix permission settings outside snap hooks
* Fix permissions of export files
