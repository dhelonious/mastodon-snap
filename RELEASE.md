# Unofficial Snap for Mastodon 4.4.2

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.4.2

This release also includes:

* ffmpeg 7.1.1
* libvips 8.17.1
* nginx 1.29.0
* node 20.19.4
* postgres 17.5
* redis 8.0.3
* ruby 3.4.4

Changelog for 4.4.2snap1:

* Add proper support for reverting the snap
* Improve the restore script to be independent of the setup script
* Update node to 20.19.4
* Update bird-ui to 2.3.3
* Update tangerine-ui to 2.4.4

⚠️ Upgrade notes ⚠️

* Rolling updates from versions earlier than Mastodon 4.3 are not supported
* Import jobs from Mastodon versions earlier than Mastodon 4.2 are not supported
* Requires updating the metadata for the Elasticsearch accounts index

> [!NOTE]
> As of release `4.4.0snap1`, the Fediday and Snow addons have been removed.
