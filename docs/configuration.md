# ⚙️ Configuration

Basic settings can be configured using key-value pairs:

    sudo snap set mastodon-server KEY=VALUE

The following settings are available:

| Key                   | Values                        | Default value          | Description                                                                          |
|-----------------------|-------------------------------|------------------------|--------------------------------------------------------------------------------------|
| `domain`              | valid FQDN                    |                        | FQDN of the Mastodon instance                                                        |
| `email`               | valid e-mail                  |                        | E-mail address of the owner of the Mastodon instance                                 |
| `ports.http`          | 0 to 65353                    | 80                     | HTTP port                                                                            |
| `ports.https`         | 0 to 65353                    | 443                    | HTTPS port                                                                           |
| `acme.server`         | letsencrypt, zerossl, buypass | letsencrypt            | CA used for acquiring an SSL certificate, see [acme.sh server](https://github.com/acmesh-official/acme.sh/wiki/Server) |
| `update.backup`       | true, false                   | true                   | Create a backup in `/var/snap/mastodon-server/common/update/backups` before updating |
| `update.announcement` | true, false                   | true                   | Create an announcement 3 minutes before the snap is updated and publish new version  |
| `status.length`       | integer                       | 1000                   | Character limit of statuses (toots); changes require recompilation of assets [1]     |
| `media.dir`           | absolute path                 | `$SNAP_COMMON/media`   | Location of the media directory (*public/system*)                                    |
| `backup.dir`          | absolute path                 | `$SNAP_COMMON/backups` | Location of the backup directory                                                     |
| `backup.days`         | integer                       | 0                      | Create and keep backups for `backup.days` (enabled if > 0)                           |
| `cleanup.days`        | integer                       | 3                      | Cleanup media and statuses older than `cleanup.days` (enabled if > 0)                |
| `cleanup.media`       | true, false                   | true                   | Cleanup media files, see [tootctl media remove](https://docs.joinmastodon.org/admin/tootctl/#media-remove) |
| `cleanup.headers`     | true, false                   | true                   | Cleanup headers, see [tootctl media remove](https://docs.joinmastodon.org/admin/tootctl/#media-remove) |
| `cleanup.previews`    | true, false                   | true                   | Cleanup preview cards, see [tootctl preview_cards remove](https://docs.joinmastodon.org/admin/tootctl/#preview_cards) |
| `cleanup.statuses`    | true, false                   | true                   | Cleanup unreferenced statuses, see [tootctl statuses remove](https://docs.joinmastodon.org/admin/tootctl/#statuses-remove) |
| `cleanup.orphans`     | true, false                   | false                  | Cleanup orphaned media files, see [tootctl media remove-orphans](https://docs.joinmastodon.org/admin/tootctl/#media-remove-orphans) |
| `cleanup.accounts`    | true, false                   | false                  | Cleanup user accounts, see [tootctl accounts delete](https://docs.joinmastodon.org/admin/tootctl/#accounts-delete) |
| `log.access.enabled`  | true, false                   | false                  | Logging of http(s) accesses                                                          |
| `log.access.format`   | standard, network, private    | network                | Use of real/network/no IP addresses in the access log                                |

[1] Changing this value will increase the time it takes for snapcraft to update this snap. This will increase the downtime of your instance by about 5 minutes.

You can also set multiple values at once using

    sudo snap set mastodon-server KEY1=VALUE1 KEY2=VALUE2

Configuration files can be used for further customization.

## Single user instances

If you plan to use your instance for yourself only, you may want to enable `SINGLE_USER_MODE` in `/var/snap/mastodon-server/common/mastodon.conf`. This will disable registrations on your instance. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#single_user_mode) for more information.

## Data privacy

By default, this snap will not log accesses unless `log.access.enabled` is `true`. Otherwise, the IP addresses in the access logs are anonymized by removing the last octet of each IP address (e.g. 192.168.100.10 becomes 192.168.100.0). If you want to change this, for example for debugging or to use [fail2ban](https://github.com/fail2ban/fail2ban), you can set `log.access.format` to `standard`.

> Note that even if access logging is enabled and not anonymized, the log files are rotated daily and anonymized.

Also, to allow Mastodon to store IP addresses, you need to increase the value (in seconds) of `IP_RETENTION_PERIOD` in `/var/snap/mastodon-server/common/mastodon.conf`. For example, to set the retention period to 24 hours, use:

    IP_RETENTION_PERIOD=86400

You may also be interested in enabling what is also known as *secure mode* via `AUTHORIZED_FETCH`. This setting prevents unauthenticated access to your instances at the cost of some computational overhead. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#authorized_fetch) for more details.

## Mail

Add the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    SMTP_SERVER=smtp.example.com
    SMTP_PORT=465
    SMTP_LOGIN=mastodon@example.com
    SMTP_PASSWORD=********
    SMTP_AUTH_METHOD=plain
    SMTP_SSL=true
    SMTP_OPENSSL_VERIFY_MODE=none
    SMTP_ENABLE_STARTTLS=always
    SMTP_FROM_ADDRESS="Mastodon <mastodon@example.com>"

> Note that SMTP is not necessarily required for a single user instance. However, the use of an SMTP service is highly recommended when running a server.

## Elasticsearch

Elasticsearch provides some advanced search features and is required for the posts to be searchable at all. Due to its size, Elasticsearch is not included in this snap. An [external installation](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html) can be used by adding the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    ES_ENABLED=true
    ES_HOST=localhost
    ES_PORT=9200
    ES_PRESET=single_node_cluster
    ES_USER=elastic
    ES_PASS=********

> Note: `ES_USER` and `ES_PASS` are required if `xpack.security` is enabled in `/etc/elasticsearch/elasticsearch.yml` (see [docs.joinmastodon.org/admin/elasticsearch](https://docs.joinmastodon.org/admin/elasticsearch/#security) for details).

Create the elasticsearch indexes using the following command:

    mastodon-server.tootctl search deploy

## S3 Storage

Add the following lines to `/var/snap/mastodon-server/common/mastodon.conf`:

    S3_ENABLED=true
    S3_FORCE_SINGLE_REQUEST=true
    S3_HOSTNAME=s3.example.com
    S3_ENDPOINT=https://s3.example.com
    S3_BUCKET=mastodon
    AWS_ACCESS_KEY_ID=********
    AWS_SECRET_ACCESS_KEY=********

> Note: `S3_FORCE_SINGLE_REQUEST` allows Mastodon to handle large uploads properly. See [docs.joinmastodon.org/admin/config](https://docs.joinmastodon.org/admin/config/#s3) for a full list of options.

The [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) must allow for objects to be publicly readable. This is an example of a minimal policy that works:

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Principal": {
            "AWS": "*"
          },
          "Effect": "Allow",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::mastodon-server/*"
        }
      ]
    }

## Translation backend

Since version 4.0 Mastodon can use [DeepL](https://www.deepl.com) and [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) to translate toots automatically.

The following configuration variables can be used in `/var/snap/mastodon-server/common/mastodon.conf` to enable the backend:

* DeepL: [`deepl_api_key`](https://docs.joinmastodon.org/admin/config/#deepl_api_key) and [`deepl_plan`](https://docs.joinmastodon.org/admin/config/#deepl_plan)
* LibreTranslate: [`libre_translate_endpoint`](https://docs.joinmastodon.org/admin/config/#libre_translate_endpoint) and [`libre_translate_api_key`](https://docs.joinmastodon.org/admin/config/#libre_translate_api_key)

> Note that LibreTranslate is not included in this snap due to its size.

## Reverse proxy

Mastodon snap can also be used behind a reverse proxy along with other web services. In this case, SSL must not be enabled because SSL termination is done at the reverse proxy. Also, `ports.http` should be changed from the default (e.g. to `ports.http=81`).

Here is a sample configuration for an nginx reverse proxy:

    upstream mastodon {
        zone upstreams 64K;
        server 127.0.0.1:81 max_fails=1 fail_timeout=2s;
        keepalive 2;
    }

    server {
        listen 80;
        server_name example.com;
        access_log /var/log/nginx/example.com.access.log;
        error_log /var/log/nginx/example.com.error.log;

        location /.well-known/ {
            proxy_pass http://mastodon/.well-known/;
        }

        return 301 https://social.dhelonious.de;
    }

    server {
        listen 443 ssl;
        server_name example.com;
        access_log /var/log/nginx/example.com.access.log;
        error_log /var/log/nginx/example.com.error.log;

        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf;
        ssl_dhparam /etc/ssl/certs/dhparam.pem;

        add_header Strict-Transport-Security "max-age=15768000; includeSubDomains" always;
        add_header Front-End-Https on;

        client_max_body_size 0;

        location / {
            proxy_pass http://mastodon/;

            proxy_http_version 1.1;
            proxy_pass_header Server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Content-Type-Options "nosniff";
            proxy_set_header X-Robots-Tag "noindex,nofollow";
            proxy_set_header X-Frame-Options "SAMEORIGIN";
            proxy_set_header X-XSS-Protection "1; mode=block";
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
        }
    }

## External media storage

The media directory can grow quickly, depending on how busy your server is. To move the media directory to an external volume mounted under `/media` or `/mnt`, you must first allow snap access to external media:

    sudo snap connect mastodon-server:removable-media

If the default media dir `/var/snap/mastodon-server/common/media` already contains files, you can transfer them to your external directory:

    sudo rsync -a /var/snap/mastodon-server/common/media /media/mastodon

Change the `media.dir` settings to your external directory:

    sudo set mastodon-server media.dir=/media/mastodon

You can then remove the old media directory.
