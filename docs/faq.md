# ❓ FAQs

## Why use Canonical's Snap packaging?

The reason is that Snaps are more suitable for headless server applications than other packaging tools such as flatpak. All the tools used to build and run them, [Snapcraft](https://github.com/canonical/snapcraft) and [snapd](https://github.com/canonical/snapd), are open source and can be used offline. The only centralized and proprietary part of the ecosystem is the Snap Store. The store makes distribution, installation and updates much easier, especially for inexperienced users. But the Snap is also built and distributed separately on GitHub. Or you can build the Snaps locally, it's up to you.

## Why doesn't the setup command accept my account name?

Mastodon reserves some usernames for internal use. Currently these are:

* root
* admin
* administrator
* mod
* moderator
* support
* help
* webmaster

Simply choose a different name to complete the setup process.
