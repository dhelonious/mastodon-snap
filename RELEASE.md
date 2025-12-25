# Unofficial Snap for Mastodon 4.5.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.5.3

This release also includes:

* ffmpeg 8.0.1
* libvips 8.18.0
* nginx 1.29.4
* node 20.19.6
* postgres 18.1
* redis 8.4.0
* ruby 3.4.7

Changelog for 4.5.3snap3:

* Update libvips to 8.18.0
* Add improved Fediday feature (see [docs/features.md](docs/features.md))
* Improve security of nginx
* Add automatic performance tuning and scaling for PostgreSQL, Nginx and Mastodon based on the available RAM and number of CPUS
* Adds automatic performance tuning and scaling for PostgreSQL, Nginx and Mastodon based on available RAM and number of CPUS.
* Adds the `system.cpu`, `system.ram` and `system.ssd` settings.
* Adds the `mastodon-server.tune` command to update configurations after tuning
* Adds the `mastodon-server.debug-report` command.
* Add `mastodon-server.debug-report` command
* Add `pgbouncer` for database connection pooling
