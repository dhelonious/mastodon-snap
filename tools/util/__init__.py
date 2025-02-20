import hashlib
import requests

from .dependencies import dependencies_regexes, get_dependencies_urls


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

def read_snapcraft_yaml():
    with open("snap/snapcraft.yaml", "r", encoding="utf-8") as yaml_file:
        return yaml_file.read()
