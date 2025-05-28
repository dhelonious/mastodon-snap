# 🔨 Build the Snap file locally

It is also possible to build the Snap file yourself:

1. Clone this repository:

    git clone https://github.com/dhelonious/mastodon-server

2. Build the Snap by running

    snapcraft

in the repository's root directory.

> [!NOTE]
> Snapcraft relies on either `multipassd` or `lxd` to create Snaps inside a virtual machine. Therefore, Snaps cannot be created on a virtual infrastructure that does not support nested virtualization.
