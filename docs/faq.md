# ❓ FAQs


## Why is yet another method of setting up Mastodon needed?

The [Fediverse](https://en.wikipedia.org/wiki/Fediverse) is intended to remove the dependency on a single service provider. But users are still dependent on the instance providers. While a user can register with multiple instances and switch between them, their data is still tied to one instance at a time. In addition, users still do not have full control over their own data.

So anyone should be able to host their own Mastodon instance on a home server, an old PC, a VPS or even a RasPi. However, creating a Mastodon instance requires some advanced knowledge and skills. The officially provided [Docker Compose file](https://github.com/mastodon/mastodon/blob/main/docker-compose.yml) reduces the complexity by a good amount. However, some knowledge of Docker and some occasional debugging is still required.

One solution to this problem is provided by [YunoHost](https://yunohost.org), which offers a large catalog of applications, including Mastodon, that can be deployed with a single click. This makes self-hosting convenient and nearly maintenance-free. However, to ensure stability and compatibility across all these applications, YunoHost may not always be able to use the latest versions of its dependencies. This may mean that you cannot use the latest version of Mastodon or its newest features.

This brings us back to why this project was started in the first place. This standalone, all-in-one Snap package further simplifies the installation process for Mastodon, enabling anyone to host their own fully functional (micro)instance on any Linux system. Because Snaps are self-updating, setting up a Mastodon instance can be reduced to executing two simple commands, with minimal future maintenance required.


## Why use Canonical's Snap packaging instead of Flatpak?

The reason is that Snaps are more suitable for headless server applications than other packaging tools such as Flatpak. All the tools used to build and run them, [Snapcraft](https://github.com/canonical/snapcraft) and [snapd](https://github.com/canonical/snapd), are open source and can be used offline. The only centralized and proprietary part of the ecosystem is the Snap Store. The store makes distribution, installation and updates much easier, especially for inexperienced users. But the Snap is also built and distributed separately on GitHub. Or you can build the Snaps locally, it's up to you.


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
