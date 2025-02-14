#!/bin/bash
# Download the latest build artifact

REPO="dhelonious/mastodon-snap"
ACCESS_TOKEN="github_pat_XXXXXX" # Replace this with your personal access token
LATEST_ARTIFACT=$(curl -sL -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $ACCESS_TOKEN" "https://api.github.com/repos/$REPO/actions/artifacts" | jq -r ".artifacts[0].archive_download_url")

echo Downloading latest snap from $REPO
curl -LH "Authorization: Bearer $ACCESS_TOKEN" --progress-bar "$LATEST_ARTIFACT" -o /tmp/snap.zip

if unzip -o /tmp/snap.zip; then
     echo "Artifact has been downloaded successfully"
else
    echo "No artifact to download"
fi

rm -fr /tmp/snap.zip
