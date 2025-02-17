#!/bin/env python

"""
Get vulnerabilities of dependencies
"""

import requests

from pkg_resources import parse_version as vers


def get_vulnerabilities(name, version):
    url = "https://api.osv.dev/v1/query"
    data = {
        "package": {"name": name},
        "version": version,
    }

    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []

    vulnerabilities = response.json().get("vulns", [])

    matching_versions = []
    for vuln in vulnerabilities:
        cves = vuln.get("aliases", [])
        severity = vuln.get("database_specific", {}).get("severity")
        description = vuln.get("details", "")

        references = []
        for ref in vuln.get("references", []):
            url = ref.get("url")
            if url:
                references.append(url)

        for affected in vuln.get("affected", []):
            for range in affected.get("ranges", []):
                closest_version = None

                for event in range.get("events", []):
                    introduced = event.get("introduced")
                    fixed = event.get("fixed")

                    if introduced in ["0", None]:
                        continue

                    if (vers(version) >= vers(introduced) and (fixed in ["0", None] or vers(version) <= vers(fixed))):
                        if closest_version is None or vers(closest_version) < vers(introduced):
                            closest_version = introduced

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


for vulnerability in get_vulnerabilities("mastodon", "4.2.1"):
    print(vulnerability)
