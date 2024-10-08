# Unofficial snap for Mastodon 4.3.0

⚠️ Requires rebuilding Elasticsearch accounts index: `mastodon-server.tootctl search deploy --only=accounts`
⚠️ StatsD integration has been removed, replaced by OpenTelemetry integration
ℹ️ The logging format of the streaming server has changed

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.0

This release also includes:

* node 20.17.0
* ruby 3.3.5
* nginx 1.27.2
* postgres 17.0
* redis 7.4.1
* libvips 8.15.3
* ffmpeg 7.1
