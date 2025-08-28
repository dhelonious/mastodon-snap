import hashlib
import requests
import re

from .dependencies import dependencies_regexes, get_dependencies_urls
from .vulnerabilities import osv_packages


HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html, application/vnd.github.v3+json",
    "Accept-Language": "en",
}


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
    return ".".join(version.split(".")[0:2])

def url_sub_version(url, local_version, version):
    return re.sub(
        r"/(v?)"+local_version.replace(".", r"\.")+r"/",
        r"/\g<1>"+version+"/",
        url,
    )

def read_snapcraft_yaml():
    with open("snap/snapcraft.yaml", "r", encoding="utf-8") as yaml_file:
        return yaml_file.read()
