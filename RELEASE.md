# Unofficial snap for Mastodon 4.3.0-rc.1

⚠️ This is a pre-release! This has not been as widely tested as regular releases, although it is still tested on mastodon.social and some other servers. If you update to this release, you will not be able to safely downgrade to the existing stable releases. You will, however, be able to upgrade to later nightly releases, prereleases as well as the upcoming 4.3.0 stable release.

⚠️ Requires rebuilding Elasticsearch accounts index: `mastodon-server.tootctl search deploy --only=accounts`
⚠️ StatsD integration has been removed, replaced by OpenTelemetry integration
ℹ️ The logging format of the streaming server has changed

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.0-rc.1

This release also includes:

* node 20.17.0
* ruby 3.3.5
* nginx 1.27.1
* postgres 17.0
* redis 7.4.0
* libvips 8.15.3
* ffmpeg 7.0.2
