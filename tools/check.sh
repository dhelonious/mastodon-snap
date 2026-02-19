#!/bin/bash

# Check envs

export envs=$(cat <<-END
src/acme/acme.env
src/logrotate/logrotate.env
src/mastodon/mastodon.env
src/nginx/nginx.env
src/pgbouncer/pgbouncer.env
src/postgres/postgres.env
src/redis/redis.env
src/snap/debug.env
src/snap/hook.env
src/snap/settings.env
src/snap/snap.env
END
)

for env in $envs; do
    bash -n "$env"
    # Alternative: shellcheck "$env"
done
