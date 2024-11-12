#!/usr/bin/env bash
#
# Run this from a branch to lift the `tiledb.cloud` -> `tiledb_cloud` move onto that branch.

if [ $# -gt 0 ]; then
  onto="$1"; shift
else
  onto="$(git rev-parse --abbrev-ref '@{u}')"
fi

if [ $# -gt 0 ]; then
  cp="$1"; shift
else
  cp="$(git log --format=%h mv.sh | tail -n1)"
fi

git reset --hard "$onto"
git cherry-pick "$cp"
./mv.sh
git commit -am '`mv.sh`'
