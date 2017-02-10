#!/usr/bin/env bash
# Install libreoffice-difftool

set -e

DIR=$1
if [ -z "$DIR" ]; then
    echo Usage: installer.sh DIRECTORY
    exit 1
fi
cp startlo.sh lodiff.py lodiff-config-repo.sh $DIR

git config --global difftool.lodiff.cmd "lodiff.py \$LOCAL \$REMOTE"
git config --global diff.odf binary true
git config --global diff.odf textconf odt2txt

echo "LibreOffice-difftool successfully installed!"
