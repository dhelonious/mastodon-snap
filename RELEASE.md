# Unofficial snap for Mastodon 4.3.3

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.3

This release also includes:

* node 20.18.2
* ruby 3.3.5
* nginx 1.27.3
* postgres 17.2
* redis 7.4.2
* libvips 8.16.0
* ffmpeg 7.1

Changelog for 4.3.3snap3:

* Improve security of nginx
* Add debug mode and `mastodon-server.debug-report` command
* Add automatic performance tuning and scaling for PostgreSQL, Nginx and Mastodon based on the available RAM and number of CPUS
* Adds automatic performance tuning and scaling for PostgreSQL, Nginx and Mastodon based on available RAM and number of CPUS.
* Adds the `system.cpu`, `system.ram` and `system.ssd` settings.
* Adds the `mastodon-server.tune` command to update configurations after tuning
* Adds the `mastodon-server.debug-report` command.
