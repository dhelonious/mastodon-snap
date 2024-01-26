#!/bin/bash

find src -type f -path "*/bin/*" -print0 | xargs -0 -n1 chmod +x

while getopts "dt" OPTION; do
  case "$OPTION" in
    d)
      snapcraft --debug | tee build.log
      exit 0
      ;;
    t)
      time unbuffer snapcraft try | tee build.log
      exit 0
      ;;
  esac
done
shift "$(($OPTIND -1))"

time unbuffer snapcraft | tee build.log
