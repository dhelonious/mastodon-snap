# Unofficial Snap for Mastodon 4.5.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.5.3

This release also includes:

* ffmpeg 8.0.1
* libvips 8.18.0
* nginx 1.29.4
* node 20.19.6
* pgbouncer 1.25.1
* postgres 18.1
* redis 8.4.0
* ruby 3.4.7

Changelog for 4.5.3snap3:

* Update libvips to 8.18.0
* Add pgbouncer for database connection pooling
* Split sidekiq into prioritised processes (`sidekiq-high`, `sidekiq-medium`, and `sidekiq-low`)
* Improve the security of nginx
* The `mastodon-server.debug-report` command has been added
* Add automatic performance tuning and scaling for PostgreSQL, Nginx and Mastodon, based on available RAM and the number of CPUs. The settings `system.cpu`, `system.ram` and `system.ssd` have been added, as well as the `mastodon-server.tune` command.
* Add an improved Fediday feature (see [docs/features.md](docs/features.md))
* Use `logs` and `announcements` as the settings names instead of `log` and `announcement` (see [docs/configuration.md](docs/configuration.md))
