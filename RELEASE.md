# Unofficial Snap for Mastodon 4.4.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.4.3

This release also includes:

* ffmpeg 8.0
* libvips 8.17.1
* nginx 1.29.1
* node 20.19.4
* postgres 17.6
* redis 8.2.1
* ruby 3.4.4

Changelog for 4.4.3snap3:

* Update yarn to 4.9.4
* Disable `client_max_body_size` in nginx settings

⚠️ Upgrade notes ⚠️

* Rolling updates from versions earlier than Mastodon 4.3 are not supported
* Import jobs from Mastodon versions earlier than Mastodon 4.2 are not supported
* Requires updating the metadata for the Elasticsearch accounts index

> [!NOTE]
> As of release `4.4.0snap1`, the Fediday and Snow addons have been removed.
