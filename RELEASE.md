# Unofficial snap for Mastodon 4.3.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.3

This release also includes:

* node 20.18.3
* ruby 3.3.5
* nginx 1.27.4
* postgres 17.3
* redis 7.4.2
* libvips 8.16.0
* ffmpeg 7.1

Changelog for 4.3.3snap3:

* Rename the `log.access.format` options to:
  - `standard`: all IP addresses are logged
  - `network`: only the network addresses are logged (default)
  - `private`: no IP addresses are logged
* Upgrade of node to 20.18.3
* Upgrade of nginx to 1.27.4
* Upgrade of postgres to 17.3
