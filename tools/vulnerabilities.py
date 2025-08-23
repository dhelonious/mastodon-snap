#!/bin/env python

"""
Get vulnerabilities of dependencies
"""

import re
import argparse
import requests

from packaging.version import parse as vers
from util import (
    HEADERS,
    dependencies_regexes,
    read_snapcraft_yaml,
)


parser = argparse.ArgumentParser(description="Get vulnerabilities of dependencies")
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

def print_table_header():
    if args.markdown:
        print("| Name | Local version | Fixed version | Severity | CVEs |")
        print("| :--- | :---: | :---: | :---: | :--- |")
    else:
        print(f"{'Name':<15} {'Local version':<15} {'Fixed version':<15} {'Severity':<10} CVEs")
        print(f"{'='*15} {'='*15} {'='*15} {'='*10} {'='*20}")

def print_table(name, version, fixed, severity, cves, **kwargs):
    if args.markdown:
        print(f"| {' | '.join([name, version, fixed, severity, ', '.join(cves)])} |")
    else:
        print(f"{name:<15} {version:<15} {fixed:<15} {severity:<10} {', '.join(cves)}")

def get_vulnerabilities(name, version):
    url = "https://api.osv.dev/v1/query"
    data = {
        "package": {"name": name},
        "version": version,
    }

    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code != 200:
        print_verbose(f"Error: {response.status_code}")
        return []

    vulns = response.json().get("vulns", [])

    matching_versions = []
    for vuln in vulns:
        cves = vuln.get("aliases", [])
        severity = vuln.get("database_specific", {}).get("severity")
        description = vuln.get("details", "")

        references = []
        for ref in vuln.get("references", []):
            url = ref.get("url")
            if url:
                references.append(url)

        for affected in vuln.get("affected", []):
            for range_ in affected.get("ranges", []):
                closest_version = None

                for event in range_.get("events", []):
                    introduced = event.get("introduced", "")
                    fixed = event.get("fixed", "")

                    if introduced in ["0", ""]:
                        continue

                    try:
                        if (vers(version) >= vers(introduced) and (fixed in ["0", ""] or vers(version) <= vers(fixed))):
                            if closest_version is None or vers(closest_version) < vers(introduced):
                                closest_version = introduced
                    except:
                        print_verbose(f"Invalid comparison: {introduced} <= {version} <= {fixed}")
                        continue

                if closest_version:
                    matching_versions.append({
                        "introduced": introduced,
                        "fixed": fixed,
                        "severity": severity,
                        "cves": cves,
                        "references": references,
                        "description": description,
                    })

    return matching_versions


snapcraft_yaml = read_snapcraft_yaml()

table = []
for name, regex in dependencies_regexes.items():
    print_silent(f"Checking {name}...")

    version = re.findall(regex, snapcraft_yaml)[0]
    print_verbose(f"-> {version}")

    vulnerabilities = get_vulnerabilities(name, version)
    for vulnerability in vulnerabilities:
        print_verbose(f"-> {', '.join(vulnerability['cves'])}")
        table.append({"name": name, "version": version, **vulnerability})

if table:
    print_verbose("Printing table...")
    print_table_header()
    for entry in table:
        print_table(**entry)
else:
    print_silent("No known vulnerabilities")
