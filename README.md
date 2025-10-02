Unofficial Snap for Mastodon (decentralized social media server) 🦣📦


# 📖 Table of contents

- [About](#-about)
- [Quickstart](#-quickstart)
- [Installation](#-installation)
  - [Online from the Snap store](#online-from-the-snap-store)
  - [Offline from a Snap file](#offline-from-a-snap-file)
  - [Updates](#updates)
  - [Revisions](#revisions)
- [Setup your instance](#-setup-your-instance)
  - [Certificates](#certificates)
  - [Backups](#backups)
  - [Themes](#themes)
- [Configuration](#️-configuration)
- [Maintenance](#-maintenance)
- [Troubleshooting](#-troubleshooting)
- [Resources](#-resources)


# 📌 About

[Mastodon](https://joinmastodon.org) is a free, open-source social network server based on [ActivityPub](https://activitypub.rocks) where users can follow friends and discover new ones. On Mastodon, users can publish anything they want: links, pictures, text, video. All Mastodon servers are interoperable as a federated network (users on one server can seamlessly communicate with users from another one, including non-Mastodon software that implements ActivityPub!)

The goal of this project is to simplify the setup of a Mastodon instance without requiring any prior knowledge of the technology behind it. This enables anyone to host their own fully functional (micro)instance with minimal future maintenance required. The all-in-one Snap package also offers support for ACME to automatically obtain SSL certificates for HTTPS.

Supported architectures:

* amd64

For more information, see the latest [release readme](RELEASE.md) or the [FAQs](docs/faq.md).


# 🚀 Quickstart

If you're not running Ubuntu, start by [installing the Snap daemon](https://snapcraft.io/docs/installing-snapd#without-snap). Then run these commands:

    sudo snap install mastodon-server

    sudo mastodon-server.setup

🥳 Congratulations! You now have your very own Mastodon instance! 🎉

> [!IMPORTANT]
> An administrator account with a randomly generated password is created during setup. Some usernames such as `admin` and `administrator` are reserved by Mastodon. See the [FAQs](docs/faq.md) for a full list.


# 📦 Installation

## Online from the Snap store

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/mastodon-server)

You can also install the Snap directly from the command line:

    sudo snap install mastodon-server

## Offline from a Snap file

If you don't want to use the Snap store, you can also download a Snap file from the [releases page](https://github.com/dhelonious/mastodon-snap/releases) and install it using:

    sudo snap install mastodon-server_VERSION_ARCH.snap --dangerous

> [!TIP]
> In this context *dangerous* only means that the Snap file is not signed. This is normal for Snaps built and distributed outside the Snap store.

> [!NOTE]
> A common criticism of Snaps is their dependence on Canonical. However, it is possible to install Snaps offline and also build them locally directly from source. See the [build instructions](docs/build.md) for how to do this.

## Updates

A Snap Store installation is automatically updated when new versions are released.

> [!NOTE]
> Be aware that there will always be a short downtime due to the way Snaps are updated.

To update your local installation, you can simply repeat the steps above with a newer version of the Snap file. This will update your Mastodon instance in-place by creating a new Snap revision.

If you have installed a Snap file locally and still want to benefit from automatic updates, you can switch to the Snap Store installation using:

    snap refresh --amend mastodon-server

After the Snap has updated itself, a new unpublished announcement will be created. You can view, publish or delete this announcement in *Preferences/Administration/Announcements*.

> [!NOTE]
> By default, `update.announcement` is enabled (see the [configuration docs](docs/configuration.md)), which will display an update announcement 5 minutes before the Snap is updated. This will prolong the time the Snap is on hold during a refresh.

### Refresh timer

If you want to control the times at which Snaps are updated, you need to change the [refresh.timer](https://snapcraft.io/docs/managing-updates#p-32248-refreshtimer):

    snap set system refresh.timer=03:00

You can check the current settings with:

    snap refresh --time

## Revisions

If a snap update fails, you can always use the `snap revert` command to [revert to an earlier revision](https://snapcraft.io/docs/managing-updates#p-32248-revert-to-an-earlier-revision).

> [!TIP]
> Use the command `snap revert mastodon-server --revision=<rev>` to select a specific [revision](https://snapcraft.io/docs/revisions). Note that the revision is *not* the version number of the snap.


# 🦣 Setup your instance

An initial setup command is required to initialize the database and configuration files for Mastodon:

    sudo mastodon-server.setup

> [!NOTE]
> Be patient if you have changed the `status.length` as it takes some time to recompile the assets, especially if there is a small amount of RAM available. Ideally these values should be changed before setup. Otherwise you may want to [increase swap space](https://www.baeldung.com/linux/increase-swap-space).

> [!TIP]
> If you're restoring your instance from a backup, use the `mastodon-server.restore` command directly. See the [backups guide](docs/backups.md)) for more information.

## Certificates

SSL certificates can be obtained via ACME from either [Let's Encrypt](https://letsencrypt.org/), [ZeroSSL](https://zerossl.com/) or [BuyPass](https://buypass.com). This is done either during `mastodon-server.setup` or by using:

    mastodon-server.get-certificate

Use the `acme.server` setting to select the CA (see the [configuration docs](docs/configuration.md)).

> [!NOTE]
> `get-certificate` will automatically enable HTTPS on port `ports.https`.

> [!IMPORTANT]
> HTTP is no longer supported in production. Mastodon will always serve https:// links.

See the [certificates docs](docs/certificates.md) for advanced certificate topics.

## Backups

Read the [backups guide](docs/backups.md) to learn how to export and restore your Mastodon server.

## Themes

Coming from ~~Twitter~~ X and wanting a familiar look? Then the included [Mastodon Bird UI](https://github.com/ronilaukkarinen/mastodon-bird-ui) and [Tangerine UI](https://github.com/nileane/TangerineUI-for-Mastodon) themes might be for you. While *Mastodon Bird UI* retains the separation between dark, light and high contrast variants, *Tangerine UI* automatically switches to a light or dark variant depending on what your browser requests. You can change the theme in *Preferences/Appearance*.

> [!IMPORTANT]
> If you have a severe visual impairment, an [accessible version of the Bird UI theme](https://github.com/ronilaukkarinen/mastodon-bird-ui#how-to-install-an-accessible-version-built-for-people-with-serious-vision-impairment) is included by default with an increased font size. This theme is indicated by the phrase ***High contrast++***, which contains ***two plus signs*** and is translated into your selected language. In addition, this theme is marked with the ♿ ***emoji representing a person in a wheelchair*** as the [International Symbol of Access](https://en.wikipedia.org/wiki/International_Symbol_of_Access).


# ⚙️ Configuration

The command

    mastodon-server.tootctl

replaces the `sudo -u mastodon RAILS_ENV=production bin/tootctl` command often found in guides and documentations.

See the [configuration docs](docs/configuration.md) for a complete overview of the configuration variables and other commands.


# 🚧 Maintenance

Read the [maintenance guide](docs/maintenance.md) to learn how to access the database shell and perform other maintenance tasks on your instance.

The `mastodon-server.announce` command can be used to create automated server notifications in Mastodon.


# 🔥 Troubleshooting

If you encounter a problem, check if it has already been solved in the [troubleshooting guide](docs/troubleshooting.md). Otherwise, open a new [issue on GitHub](https://github.com/dhelonious/mastodon-snap/issues).


# 🔗 Resources

- [Fedi.Tips](https://fedi.tips/) is a valuable resource for Mastodon and the Fediverse.
- [Fedi.Directory](https://fedi.directory/) can help you find interesting accounts to follow.
- [FediDB](https://fedidb.com/) provides statistics on the Fediverse.
- [FediBuzz Relay](https://relay.fedi.buzz/) can be used to follow hashtags on other instances.
- [delightful activitypub development](https://delightful.coding.social/delightful_activitypub_development/) is a curated list of software for the Fediverse
