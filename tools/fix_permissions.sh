#!/bin/bash

find src -type f -path "*/bin/*" -print0 | xargs -0 -n1 chmod +rx
