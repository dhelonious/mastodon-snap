#!/bin/env python

import re
import requests


MASTODON_RELEASE = "v4.2.8"


def print_table(name, version):
    print(f"{name:<12} {version}")


github_latest_urls = {
    "mastodon": {
        "url": "https://github.com/mastodon/mastodon/releases/latest",
        "lstrip": "v",
    },
    "logrotate": {
        "url": "https://github.com/logrotate/logrotate/releases/latest",
    },
    "curl": {
        "url": "https://github.com/curl/curl/releases/latest",
        "lstrip": "curl-",
        "replace": ("_", "."),
    },
    "postgres": {
        "url": "https://www.postgresql.org/ftp/latest",
        "lstrip": "v",
    },
    "redis": {
        "url": "https://github.com/redis/redis/releases/latest",
    },
    "acme": {
        "url": "https://github.com/acmesh-official/acme.sh/releases/latest",
    },
    "yarn": {
        "url": "https://github.com/yarnpkg/yarn/releases/latest",
        "lstrip": "v",
    },
    "jemalloc": {
        "url": "https://github.com/jemalloc/jemalloc/releases/latest",
    },
    "imagemagick": {
        "url": "https://github.com/ImageMagick/ImageMagick/releases/latest",
    },
    "bird-ui": {
        "url": "https://github.com/ronilaukkarinen/mastodon-bird-ui/releases/latest",
    },
    "tangerine-ui": {
        "url": "https://github.com/nileane/TangerineUI-for-Mastodon/releases/latest",
        "lstrip": "v",
    },
}
nginx = {
    "url": "https://api.github.com/repos/nginx/nginx/tags",
    "lstrip": "release-",
}
openssl = {
    "url": "https://api.github.com/repos/openssl/openssl/releases",
    "regex": re.compile(r"OpenSSL (1\..+)"),
}
ruby_url = f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/.ruby-version"
node = {
    "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Vagrantfile",
    "regex": re.compile(r".*https://deb\.nodesource\.com/([A-Za-z0-9_\.]+).*"),
    "lstrip": "setup_v",
    "version_url": "https://nodejs.org/download/release/latest-v{}",
}
lib_musl = {
    "url": "https://api.github.com/repos/bminor/musl/tags", # NOTE: Unofficial mirror
    "lstrip": "v",
}
bundler = {
    "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Gemfile.lock",
    "regex": re.compile(r"BUNDLED WITH\n\s+(\d+\.\d+\.\d+)", re.MULTILINE),
}


for name, repo in github_latest_urls.items():
    r = requests.get(repo["url"], timeout=10)
    version = r.url.rstrip('/').split('/')[-1]
    if "lstrip" in repo:
        version = version.lstrip(repo["lstrip"])
    if "replace" in repo:
        version = version.replace(*repo["replace"])
    print_table(name, version)

# nginx
r = requests.get(nginx["url"], timeout=10)
nginx_tags = [d["name"] for d in r.json()]
print_table("nginx", nginx_tags[0].lstrip(nginx["lstrip"]))

# openssl
r = requests.get(openssl["url"], timeout=10)
openssl_releases = [d["name"] for d in r.json() if openssl["regex"].search(d["name"])]
print_table("openssl", openssl["regex"].match(openssl_releases[0]).group(1))

# ruby
r = requests.get(ruby_url, timeout=10)
print_table("ruby", r.text.strip())

# node
r = requests.get(node["url"], timeout=10)
node_version = node["regex"].findall(r.text)[0].lstrip(node["lstrip"])
version_regex = re.compile(f"v({node_version.replace('x', '[0-9.]+')})")
r = requests.get(node["version_url"].format(node_version), timeout=10)
print_table("node", version_regex.findall(r.text)[0])

# musl-libc
r = requests.get(lib_musl["url"], timeout=10)
lib_musl_tags = [d["name"] for d in r.json()]
print_table("musl-libc", lib_musl_tags[0].lstrip(lib_musl["lstrip"]))

# bundler
r = requests.get(bundler["url"], timeout=10)
bundler_version = bundler["regex"].findall(r.text)[0]
print_table("bundler", bundler_version)
