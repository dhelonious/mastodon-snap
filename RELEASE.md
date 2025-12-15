# Unofficial Snap for Mastodon 4.5.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.5.3

This release also includes:

* ffmpeg 8.0.1
* libvips 8.17.3
* nginx 1.29.4
* node 20.19.6
* postgres 18.1
* redis 8.4.0
* ruby 3.4.7

Changelog for 4.5.3snap2:

* Update nginx to 1.29.4
* Add the `mastodon-server.generate-wrapstodon` command to create a year-in-review report (see [docs/features.md](docs/features.md)).

> [!NOTE]
> Mastodon 4.6 will introduce an automatically generated Wrapstodon feature. However, to enable users of this snap to do so in 2025, the old, lightweight Wrapstodon implementation will be supported in version 4.5.
