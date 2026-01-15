# ❓ FAQs

## Why shouldn't I join mastodon.social?

Joining an existing instance ([mastodon.social](https://mastodon.social/) is just one example) is perfectly acceptable and should be the first step you take to explore the Fediverse. For most people, this will also be a long-term solution. Mastodon instances, especially the larger ones, are professionally hosted and maintained. Therefore, they can be considered safe and future-proof.

However, there may be reasons to consider a self-hosted approach. First and foremost, you may want total control over your data at all times, which is only possible if your data remains on a machine that you fully control. Another reason might be that you want to start an instance for your family and friends, or for like-minded individuals around a specific topic or hobby.

Lastly, you may want more control over content moderation. If your home instance blocks a particular domain, you cannot follow accounts from it or receive messages. One solution to this issue would be to switch to an instance that does not block this domain. Alternatively, you could switch to a self-hosted instance and decide which domains to block yourself. In both cases, you may wish to read this article: [Moving or leaving accounts](https://docs.joinmastodon.org/user/moving/).

## Why should I not use masto.host?

Managed services, such as those offered by [masto.host](https://masto.host/), are ideal for users who lack the means or motivation to self-host. They offer most of the above benefits, but without the burden of full responsibility for running and maintaining a Mastodon instance alone.

This is generally fine, but a few concerns should be kept in mind:

1. Running multiple instances on the same infrastructure undermines the concept of a decentralised federation. If the infrastructure becomes temporarily unavailable due to technical errors, or permanently unavailable if the business shuts down, you will not be able to access your account. Therefore, having a backup account on another instance and regularly exporting your data may be a good idea.

2. With a managed service, data access is limited because you only control the instance, not the host itself. This is the main difference between a managed service and a virtual private server (VPS). However, it should be noted that [masto.host](https://masto.host/) offers the feature of [downloading backups](https://masto.host/help/downloading-backups/).

3. To achieve true independence, it is important to maintain choices. Currently, the only managed instance providers for Mastodon are [masto.host](https://masto.host/) and [toot.io](https://toot.io/mastodon_hosting.html). This does not mean that these providers' services are bad in any way. However, you should be aware that the options are currently limited and will probably remain so in future.

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


## A user has forgotten their password. What should I do?

There are two ways to reset the password:

1. The user can click the "Forgot your password?" button and wait for the confirmation email. This method only works if SMTP is configured properly.

2. Use the following command to reset the user's password:

    mastodon-server.tootctl accounts modify <username> --reset-password

> [!TIP]
> This also works for the admin account.
