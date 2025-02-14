# 🪪 Certificates

## Provide your own certificates

If you want to provide your own certificates, you will need to place the private key and full chain certificate in the following locations:

* `/var/snap/mastodon-server/common/certs/<domain>_ecc/<domain>.key`
* `/var/snap/mastodon-server/common/certs/<domain>_ecc/fullchain.cer`

Restart the `nginx` service afterwards:

    snap restart mastodon-server.nginx
