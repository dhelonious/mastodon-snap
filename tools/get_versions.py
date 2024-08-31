#!/bin/env python

"""
Get versions of dependencies
"""

import re
import argparse
import requests


def print_table(name, version):
    print(f"{name:<12} {version}")


parser = argparse.ArgumentParser(description="Get versions of dependencies")
parser.add_argument("mastodon_version", type=str)
args = parser.parse_args()


MASTODON_RELEASE = f"v{ args.mastodon_version }"

r = requests.get(f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Vagrantfile", timeout=10)
NODE_MAJOR = re.findall(r".*NODE_MAJOR=([0-9]+).*", r.text)[0]


github_latest_urls = {
    "mastodon": {
        "url": "https://github.com/mastodon/mastodon/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/mastodon/mastodon/tags",
        "lstrip": "v",
    },
    "bird-ui": {
        "url": "https://github.com/ronilaukkarinen/mastodon-bird-ui/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/ronilaukkarinen/mastodon-bird-ui/tags",
    },
    "tangerine-ui": {
        "url": "https://github.com/nileane/TangerineUI-for-Mastodon/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/nileane/TangerineUI-for-Mastodon/tags",
        "lstrip": "v",
    },
    "node": {
        "url": "https://nodejs.org/download/release/latest-v{}.x".format(NODE_MAJOR),
        "regex": re.compile(f"v({NODE_MAJOR}.[0-9.]+)"),
    },
    "ruby": {
        "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/.ruby-version"
    },
    "bundler": {
        "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Gemfile.lock",
        "regex": re.compile(r"BUNDLED WITH\n\s+(\d+\.\d+\.\d+)", re.MULTILINE),
    },
    "yarn": {
        "url": "https://github.com/yarnpkg/berry/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/yarnpkg/berry/tags",
        "lstrip": "v",
    },
    "postgres": {
        "url": "https://www.postgresql.org/ftp/latest",
        "lstrip": "v",
    },
    "nginx": {
        "url": "https://api.github.com/repos/nginx/nginx/tags",
        "lstrip": "release-",
    },
    "redis": {
        "url": "https://github.com/redis/redis/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/redis/redis/tags",
    },
    "acme": {
        "url": "https://github.com/acmesh-official/acme.sh/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/acmesh-official/acme.sh/tags",
    },
    "logrotate": {
        "url": "https://github.com/logrotate/logrotate/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/logrotate/logrotate/tags",
    },
    "libvips": {
        "url": "https://github.com/libvips/libvips/releases/latest",
        "lstrip": "v",
    },
    "ffmpeg": {
        "url": "https://api.github.com/repos/FFmpeg/FFmpeg/tags", # NOTE: mirror
        "regex": re.compile(r"^[^0-9\.]*([0-9\.]+)[^0-9\.]*$"),
        "exclude": "dev",
    },
}


for name, repo in github_latest_urls.items():
    r = requests.get(repo["url"], timeout=10)
    version = None

    if repo["url"].endswith("latest"):
        version = r.url.rstrip("/").split("/")[-1]

    elif repo["url"].startswith("https://api.github.com"):
        tags = [d["name"] for d in r.json()]
        if "exclude" in repo:
            tags = [t for t in tags if repo["exclude"] not in t]
        if "regex" in repo:
            matches = [repo["regex"].match(t) for t in tags]
            tags = [m.group(1) for m in matches if m]
        version = sorted(tags, reverse=True)[0]

    else:
        if "regex" in repo:
            version = repo["regex"].findall(r.text)[0]
        else:
            version = r.text.strip()

    if "lstrip" in repo:
        version = version.lstrip(repo["lstrip"])
    if "replace" in repo:
        version = version.replace(*repo["replace"])

    print_table(name, version)
