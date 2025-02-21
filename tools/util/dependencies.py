import re


dependencies_regexes = {
    "acme.sh": r"https://github\.com/acmesh-official/acme\.sh/archive/refs/tags/([0-9\.]+)\.tar\.gz",
    "bird-ui": r"BIRD_UI_TAG: ([0-9a-z-\.]+)",
    "bundler": r"BUNDLER_VERSION: \"([0-9\.]+)\"",
    "ffmpeg": r"https://ffmpeg\.org/releases/ffmpeg-([0-9\.]+)\.tar\.bz2",
    "libvips": r"https://github\.com/libvips/libvips/archive/refs/tags/v([0-9\.]+)\.tar\.gz",
    "logrotate": r"https://github\.com/logrotate/logrotate/releases/download/[0-9\.]+/logrotate-([0-9\.]+)\.tar\.gz",
    "mastodon": r"https://github.com/mastodon/mastodon/archive/refs/tags/v([0-9a-z-\.]+)\.tar\.gz",
    "nginx": r"https://nginx\.org/download/nginx-([0-9\.]+)\.tar\.gz",
    "node": r"https://nodejs.org/download/release/latest-v[0-9]+\.x/node-v([0-9\.]+)-linux-x64\.tar\.gz",
    "node_arm64": r"https://nodejs.org/download/release/latest-v[0-9]+\.x/node-v([0-9\.]+)-linux-arm64\.tar\.gz",
    "postgresql": r"https://ftp\.postgresql\.org/pub/source/v[0-9\.]+/postgresql-([0-9\.]+)\.tar\.gz",
    "redis": r"https://download\.redis\.io/releases/redis-([0-9\.]+)\.tar\.gz",
    "ruby": r"https://cache\.ruby-lang\.org/pub/ruby/[0-9\.]+/ruby-([0-9\.]+)\.tar\.gz",
    "tangerine-ui": r"TANGERINE_UI_TAG: ([0-9a-z-\.]+)",
    "yarn": r"YARN_VERSION: \"([0-9\.]+)\"",
}


def get_dependencies_urls(mastodon_release, node_major):
    return {
        "acme.sh": {
            "url": "https://github.com/acmesh-official/acme.sh/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/acmesh-official/acme.sh/tags",
            "file_regex": f"source: ({dependencies_regexes['acme.sh']})",
        },
        "bird-ui": {
            "url": "https://github.com/ronilaukkarinen/mastodon-bird-ui/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/ronilaukkarinen/mastodon-bird-ui/tags",
            "file_regex": dependencies_regexes["bird-ui"],
        },
        "bundler": {
            "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ mastodon_release }/Gemfile.lock",
            "url_regex": re.compile(r"BUNDLED WITH\n\s+(\d+\.\d+\.\d+)", re.MULTILINE),
            "file_regex": dependencies_regexes["bundler"],
        },
        "ffmpeg": {
            "url": "https://api.github.com/repos/FFmpeg/FFmpeg/tags", # NOTE: mirror
            "url_regex": re.compile(r"^[^0-9\.]*([0-9\.]+)[^0-9\.]*$"),
            "file_regex": f"source: ({dependencies_regexes['ffmpeg']})",
            "exclude": "dev",
        },
        "libvips": {
            "url": "https://github.com/libvips/libvips/releases/latest",
            "file_regex": f"source: ({dependencies_regexes['libvips']})",
            "lstrip": "v",
        },
        "logrotate": {
            "url": "https://github.com/logrotate/logrotate/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/logrotate/logrotate/tags",
            "file_regex": f"source: ({dependencies_regexes['logrotate']})",
        },
        "mastodon": {
            "url": "https://github.com/mastodon/mastodon/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/mastodon/mastodon/tags",
            "file_regex": f"source: ({dependencies_regexes['mastodon']})",
            "lstrip": "v",
        },
        "nginx": {
            "url": "https://api.github.com/repos/nginx/nginx/tags",
            "file_regex": f"source: ({dependencies_regexes['nginx']})",
            "lstrip": "release-",
        },
        "node": {
            "url": "https://nodejs.org/download/release/latest-v{}.x".format(node_major),
            "url_regex": re.compile(f"v({node_major}.[0-9.]+)"),
            "file_regex": f"source=\"({dependencies_regexes['node']})\"",
        },
        "node_arm64": {
            "url": "https://nodejs.org/download/release/latest-v{}.x".format(node_major),
            "url_regex": re.compile(f"v({node_major}.[0-9.]+)"),
            "file_regex": f"source=\"({dependencies_regexes['node']})\"",
        },
        "postgresql": {
            "url": "https://www.postgresql.org/ftp/latest",
            "file_regex": f"source: ({dependencies_regexes['postgresql']})",
            "lstrip": "v",
        },
        "redis": {
            "url": "https://github.com/redis/redis/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/redis/redis/tags",
            "file_regex": f"source: ({dependencies_regexes['redis']})",
        },
        "ruby": {
            "url": f"https://raw.githubusercontent.com/mastodon/mastodon/{ mastodon_release }/.ruby-version",
            "file_regex": f"source: ({dependencies_regexes['ruby']})",
        },
        "tangerine-ui": {
            "url": "https://github.com/nileane/TangerineUI-for-Mastodon/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/nileane/TangerineUI-for-Mastodon/tags",
            "file_regex": dependencies_regexes["tangerine-ui"],
            "lstrip": "v",
        },
        "yarn": {
            "url": "https://github.com/yarnpkg/berry/releases/latest",
            # NOTE: tag -> "url": "https://api.github.com/repos/yarnpkg/berry/tags",
            "file_regex": dependencies_regexes["yarn"],
            "lstrip": "v",
        },
    }
