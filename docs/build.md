# 🔨 Build the snap file locally

It is also possible to build the snap file yourself:

1. Clone this repository:

    git clone https://github.com/dhelonious/mastodon-server

2. Build the snap by running

    snapcraft

in the repository's root directory.

> [!NOTE]
> Snapcraft relies on either `multipassd` or `lxd` to create snaps inside a virtual machine. Therefore, snaps cannot be created on a virtual infrastructure that does not support nested virtualization.
