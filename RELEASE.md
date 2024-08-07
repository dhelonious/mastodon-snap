# Unofficial snap for Mastodon 4.2.10

⚠️ This release is an important security release fixing a major security issue.

See also the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.2.10

This release contains:

* Mastodon 4.2.10
* Node 16.20.2 (see [#25787](https://github.com/mastodon/mastodon/discussions/25787#discussioncomment-6382898))
* Ruby 3.2.3
* Bundle 2.4.13
* Yarn 1.22.22
* Nginx 1.27.0
* PostgreSQL 16.3
* Redis 7.4.0
* Acme.sh 3.0.7
* ImageMagick 7.1.1-36
* OpenSSL 1.1.1w
* Curl 8.9.1
* Logrotate 3.22.0
* Jemalloc 5.3.0
* musl-libc 1.2.5
* mastodon-bird-ui 1.8.5
* tangerine-ui 1.9.5

Changelog for 4.2.10snap4:

* Adds an option to change the character counter of toots (`status.chat-counter`).
* Moves recompile step to the stop-action of the Mastodon backend service.
* Updates some dependencies.
