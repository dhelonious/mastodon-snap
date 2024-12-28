# Unofficial snap for Mastodon 4.3.2

See the release notes for Mastodon: https://github.com/mastodon/mastodon/releases/tag/v4.3.2

This release also includes:

* node 20.18.1
* ruby 3.3.5
* nginx 1.27.3
* postgres 17.2
* redis 7.4.1
* libvips 8.16.0
* ffmpeg 7.1

## Changelog for 4.3.2snap3: Let it snow! ❄️

* Adds snow to the Mastodon UI between Christmas and New Year! (Thanks to [Roni Laukkarinen](https://github.com/ronilaukkarinen)!)
* Admin account is created during setup
* Remove the `status.char-counter` option and rename `status.char-limit` to `status.length`
* Additional improvements were added to the `mastodon-server.setup` script
* Mastodon Bird UI has been updated to 2.1.1

## Upgrade notes

Due to the changes described above, you may need to manually change the `status.length` option after the upgrade, e.g:

    snap set mastodon-server status.length=5000

However, the new default value of `status.length=1000` doubles Mastodon's default value of 500 and should be sufficient for most users.

You can also clean up the old snap variables with:

    snap unset mastodon-server status.char-limit status.char-counter
