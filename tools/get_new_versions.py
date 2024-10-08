#!/bin/env python

"""
Get versions of dependencies
"""

import re
import argparse
import hashlib
import requests


parser = argparse.ArgumentParser(description="Get versions of dependencies")
parser.add_argument("mastodon_version", type=str)
args = parser.parse_args()

MASTODON_RELEASE = f"v{ args.mastodon_version }"
with requests.get(f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Vagrantfile", timeout=10) as r:
    NODE_MAJOR = re.findall(r".*NODE_MAJOR=([0-9]+).*", r.text)[0]

dependencies = {
    "mastodon": {
        "url": "https://github.com/mastodon/mastodon/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/mastodon/mastodon/tags",
        "lstrip": "v",
        "local_regex": r"source: (https://github.com/mastodon/mastodon/archive/refs/tags/v([0-9a-z-\.]+)\.tar\.gz)",
    },
    "bird-ui": {
        "url": "https://github.com/ronilaukkarinen/mastodon-bird-ui/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/ronilaukkarinen/mastodon-bird-ui/tags",
        "local_regex": r"BIRD_UI_TAG: ([0-9a-z-\.]+)",
    },
    "tangerine-ui": {
        "url": "https://github.com/nileane/TangerineUI-for-Mastodon/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/nileane/TangerineUI-for-Mastodon/tags",
        "lstrip": "v",
        "local_regex": r"TANGERINE_UI_TAG: ([0-9a-z-\.]+)",
    },
    "node": {
        "url": "https://nodejs.org/download/release/latest-v{}.x".format(NODE_MAJOR),
        "regex": re.compile(f"v({NODE_MAJOR}.[0-9.]+)"),
        "local_regex": r"source=\"(https://nodejs.org/download/release/latest-v[0-9]+\.x/node-v([0-9\.]+)-linux-x64\.tar\.gz)\"",
    },
    "ruby": {
        "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/.ruby-version",
        "local_regex": r"source: (https://cache\.ruby-lang\.org/pub/ruby/[0-9\.]+/ruby-([0-9\.]+)\.tar\.gz)",
    },
    "bundler": {
        "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Gemfile.lock",
        "regex": re.compile(r"BUNDLED WITH\n\s+(\d+\.\d+\.\d+)", re.MULTILINE),
        "local_regex": r"BUNDLER_VERSION: \"([0-9\.]+)\"",
    },
    "yarn": {
        "url": "https://github.com/yarnpkg/berry/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/yarnpkg/berry/tags",
        "lstrip": "v",
        "local_regex": r"YARN_VERSION: \"([0-9\.]+)\"",
    },
    "postgres": {
        "url": "https://www.postgresql.org/ftp/latest",
        "lstrip": "v",
        "local_regex": r"source: (https://ftp\.postgresql\.org/pub/source/v[0-9\.]+/postgresql-([0-9\.]+)\.tar\.gz)",
    },
    "nginx": {
        "url": "https://api.github.com/repos/nginx/nginx/tags",
        "lstrip": "release-",
        "local_regex": r"source: (https://nginx\.org/download/nginx-([0-9\.]+)\.tar\.gz)",
    },
    "redis": {
        "url": "https://github.com/redis/redis/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/redis/redis/tags",
        "local_regex": r"source: (https://download\.redis\.io/releases/redis-([0-9\.]+)\.tar\.gz)",
    },
    "acme": {
        "url": "https://github.com/acmesh-official/acme.sh/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/acmesh-official/acme.sh/tags",
        "local_regex": r"source: (https://github\.com/acmesh-official/acme\.sh/archive/refs/tags/([0-9\.]+)\.tar\.gz)",
    },
    "logrotate": {
        "url": "https://github.com/logrotate/logrotate/releases/latest",
        # NOTE: tag -> "url": "https://api.github.com/repos/logrotate/logrotate/tags",
        "local_regex": r"source: (https://github\.com/logrotate/logrotate/releases/download/[0-9\.]+/logrotate-([0-9\.]+)\.tar\.gz)",
    },
    "libvips": {
        "url": "https://github.com/libvips/libvips/releases/latest",
        "lstrip": "v",
        "local_regex": r"source: (https://github\.com/libvips/libvips/archive/refs/tags/v([0-9\.]+)\.tar\.gz)",
    },
    "ffmpeg": {
        "url": "https://api.github.com/repos/FFmpeg/FFmpeg/tags", # NOTE: mirror
        "regex": re.compile(r"^[^0-9\.]*([0-9\.]+)[^0-9\.]*$"),
        "exclude": "dev",
        "local_regex": r"source: (https://ffmpeg\.org/releases/ffmpeg-([0-9\.]+)\.tar\.bz2)",
    },
}

with open("snap/snapcraft.yaml", "r", encoding="utf-8") as yaml_file:
    snapcraft_yaml = yaml_file.read()


def print_table_header():
    print(f"{'Name':<15} {'Local version':<15} {'New version':<15} SHA256 Checksum")

def print_table(name, local_version, new_version, checksum=""):
    if version != local_version:
        print(f"{name:<15} {local_version:<15} {new_version:<15} {checksum}")

def sha256_checksum(url):
    sha256 = hashlib.sha256()

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=8192):
            sha256.update(chunk)

    return sha256.hexdigest()

def major(version):
    return ".".join(version.split(".")[0])

def minor(version):
    return ".".join(version.split(".")[0:1])


print_table_header()

for name, settings in dependencies.items():
    r = requests.get(settings["url"], timeout=10)
    version = None

    if settings["url"].endswith("latest"):
        version = r.url.rstrip("/").split("/")[-1]

    elif settings["url"].startswith("https://api.github.com"):
        tags = [d["name"] for d in r.json()]
        if "exclude" in settings:
            tags = [t for t in tags if settings["exclude"] not in t]
        if "regex" in settings:
            matches = [settings["regex"].match(t) for t in tags]
            tags = [m.group(1) for m in matches if m]
        version = sorted(tags, reverse=True)[0]

    else:
        if "regex" in settings:
            version = settings["regex"].findall(r.text)[0]
        else:
            version = r.text.strip()

    if "lstrip" in settings:
        version = version.lstrip(settings["lstrip"])
    if "replace" in settings:
        version = version.replace(*settings["replace"])

    local_source = re.findall(settings["local_regex"], snapcraft_yaml)[0]
    if isinstance(local_source, str):
        local_version = local_source
        checksum = ""
    else:
        local_version = local_source[1]
        url = local_source[0]
        url = url.replace(local_version, version)
        url = url.replace(minor(local_version), minor(version))
        url = url.replace(major(local_version), major(version))
        checksum = sha256_checksum(url)

    print_table(name, local_version, version, checksum)
