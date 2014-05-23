#!/usr/bin/env bash

cat repoconf >> $1/.git/config
cat repoattributes >> $1/.gitattributes
