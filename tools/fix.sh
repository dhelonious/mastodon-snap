#!/bin/bash
# Fix snap files in the repository

echo "Make all scripts in */bin executable"
find src -type f -path "*/bin/*" -exec chmod +x {} \;

