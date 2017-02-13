#!/usr/bin/env bash

# Configure a repository for libreoffice-diff
# Usage: lodiff-config-repo.sh [DIRECTORY]
# Default is current directory

DIR=.
if [ -n "$1" ]; then
   DIR=shift
fi
cd $DIR

git config --local diff.tool lodiff
cat <<EOF >> $DIR/.gitattributes
*.odt diff=odf
*.ods diff=odf
*.odp diff=odf
EOF
