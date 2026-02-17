#!/bin/bash
# Build snap locally with improved output

NAME=$(sed -rn "s/^name: (.+)$/\1/p" snap/snapcraft.yaml)
VERSION=$(sed -rn "s/^version: (.+)$/\1/p" snap/snapcraft.yaml)

find src -type f -path "*/bin/*" -exec chmod +x {} \;

time unbuffer snapcraft --verbosity=debug | tee build.log

if ! [ -z "$(find . -name ${NAME}_${VERSION}_*.snap -type f -newermt '10 seconds ago')" ]; then
  echo
  echo Missing dependencies:
  sed -rn "s/^[0-9-]+ [0-9:\.]+ - library: (.+ missing dependency '.+').*$/* \1/p" build.log
  echo
  echo Unused libraries:
  sed -rn "s/^[0-9-]+ [0-9:\.]+ - library: (.+ unused library '.+').*$/* \1/p" build.log
  echo
  echo Files built:
  du -h ${NAME}_${VERSION}_*.snap
fi
