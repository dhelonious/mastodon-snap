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

## Changelog for 4.3.2snap6:

* Hotfix for `media.dir` setting being empty on install
* Add spinning to confetti animation
* Hotfix for `mastodon-server.get-certificate` `acme.server` check [4.3.2snap4]
* It's your Fediday: The day you joined the Fediverse will be celebrated by your instance with a confetti rain! 🎊 [4.3.2snap4]
* Support [BuyPass](https://buypass.com) SSL CA [4.3.2snap4]
* Yarn updated to 4.6.0 [4.3.2snap4]
* Let it snow: Around Christmas, snow will start falling in your Mastodon instance! ❄️ [4.3.2snap3]
* Adds snow to the Mastodon UI between Christmas and New Year! (Thanks to [Roni Laukkarinen](https://github.com/ronilaukkarinen)!) [4.3.2snap3]
* Admin account created during setup [4.3.2snap3]
* Removed the `status.char-counter` option and renamed `status.char-limit` to `status.length [4.3.2snap3]
* Additional improvements have been made to the `mastodon-server.setup` and `mastodon-server.get-certificate` scripts [4.3.2snap3]
* Mastodon Bird UI updated to 2.1.1 [4.3.2snap3]

## Upgrade notes

Due to the changes described above, you may need to manually change the `status.length` option after the upgrade, e.g:

    snap set mastodon-server status.length=5000

However, the new default value of `status.length=1000` doubles Mastodon's default value of 500 and should be sufficient for most users.

You can also clean up the old snap variables with:

    snap unset mastodon-server status.char-limit status.char-counter
