#!/bin/env python

"""
Get versions of dependencies
"""

import sys
import re
import argparse
import requests

from util import (
    sha256_checksum,
    major,
    minor,
    get_dependencies_urls,
    read_snapcraft_yaml,
)


parser = argparse.ArgumentParser(description="Get versions of dependencies")
parser.add_argument("mastodon_version", nargs="?")
parser.add_argument("-a", "--all", help="Show all versions, even if they are not out of date", action="store_true")
parser.add_argument("-v", "--verbose", help="Show additional ouptut", action="store_true")
parser.add_argument("-s", "--silent", help="Show less ouptut", action="store_true")
parser.add_argument("-m", "--markdown", help="Use markdown for table", action="store_true")
args = parser.parse_args()


def print_verbose(*line):
    if args.verbose:
        print(*line)

def print_silent(*line):
    if not args.silent:
        print(*line)

def print_error(*line):
    print(*line, file=sys.stderr)

def print_table_header():
    if args.markdown:
        print("| Name | Local version | New version | SHA256 checksum |")
        print("| :--- | :---: | :---: | :--- |")
    else:
        print(f"{'Name':<15} {'Local version':<15} {'New version':<15} SHA256 checksum")
        print(f"{'='*15} {'='*15} {'='*15} {'='*20}")

def print_table(name, local_version, new_version, checksum="", print_all=False):
    if local_version != new_version or print_all:
        if local_version != new_version and print_all:
            name += "*"
        if args.markdown:
            print(f"| {' | '.join([name, local_version, new_version, checksum])} |")
        else:
            print(f"{name:<15} {local_version:<15} {new_version:<15} {checksum}")


if args.mastodon_version:
    print_verbose("Using the given Mastodon release...")
    MASTODON_RELEASE = f"v{ args.mastodon_version }"
else:
    print_verbose("Getting the latest Mastodon release...")
    with requests.get("https://github.com/mastodon/mastodon/releases/latest", timeout=10) as r:
        if r.status_code != 200:
            print_error(r.raise_for_status())
            exit()
        else:
            MASTODON_RELEASE = r.url.rstrip("/").split("/")[-1]

print_silent(f"Use Mastodon release: {MASTODON_RELEASE}")

with requests.get(f"https://raw.githubusercontent.com/mastodon/mastodon/{ MASTODON_RELEASE }/Vagrantfile", timeout=10) as r:
    NODE_MAJOR = re.findall(r".*NODE_MAJOR=([0-9]+).*", r.text)[0]

dependencies = get_dependencies_urls(MASTODON_RELEASE, NODE_MAJOR)
snapcraft_yaml = read_snapcraft_yaml()

table = []
for name, settings in dependencies.items():
    print_silent(f"Checking {name}...")

    r = requests.get(settings["url"], timeout=10)
    print_verbose(f"{settings['url']} -> {r.status_code}")

    if r.status_code != 200:
        print_silent(r.raise_for_status())
        continue

    version = None
    if settings["url"].endswith("latest"):
        print_verbose("Using 'latest' URL...")
        version = r.url.rstrip("/").split("/")[-1]

    elif settings["url"].startswith("https://api.github.com"):
        print_verbose("Use GitHub API...")
        tags = [d["name"] for d in r.json()]
        print_verbose(f"Tags found: {tags}")
        if "exclude" in settings:
            tags = [t for t in tags if settings["exclude"] not in t]
        if "url_regex" in settings:
            matches = [settings["url_regex"].match(t) for t in tags]
            tags = [m.group(1) for m in matches if m]
        version = sorted(tags, reverse=True)[0]

    else:
        if "url_regex" in settings:
            print_verbose("Using regex on page content...")
            version = settings["url_regex"].findall(r.text)[0]
        else:
            print_verbose("Using raw page content...")
            version = r.text.strip()

    if "lstrip" in settings:
        print_verbose("Applying lstrip...")
        version = version.lstrip(settings["lstrip"])
    if "replace" in settings:
        print_verbose("Applying replace...")
        version = version.replace(*settings["replace"])
    print_verbose(f"-> {version}")

    print_verbose("Getting local version...")
    local_source = re.findall(settings["file_regex"], snapcraft_yaml)[0]
    if isinstance(local_source, str):
        local_version = local_source
        print_verbose(f"-> {local_version}")
        print_verbose("Checksum calculation not required")
        checksum = ""
    else:
        local_version = local_source[1]
        print_verbose(f"-> {local_version}")
        if version != local_version:
            url = local_source[0]
            url = url.replace(local_version, version)
            url = url.replace(minor(local_version), minor(version))
            url = url.replace(major(local_version), major(version))
            print_verbose(f"Checksum URL: {url}")
            print_verbose("Calculating checksum...")
            checksum = sha256_checksum(url)
            print_verbose(f"-> {checksum}")
        else:
            print_verbose("Checksum calculation not required")
            checksum = ""

    if local_version != version or args.all:
        table.append((name, local_version, version, checksum))

if table:
    print_verbose("Printing table...")
    print_table_header()
    for entry in table:
        print_table(*entry, print_all=args.all)
else:
    print_silent("Everything is up to date")
