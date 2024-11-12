#!/usr/bin/env bash

set -e

name="$(basename "${BASH_SOURCE[0]}")"

src=src/tiledb/cloud
dst=src/tiledb_cloud
if [ -d "$dst" ]; then
  echo "$dst exists, moving to $dst.bak" >&2
  mv "$dst"{,.bak}
fi
git mv "$src" "$dst"

git ls-files -z \
| grep -vz "^$name\$" \
| xargs -0 perl -pi -e 's/tiledb\.cloud/tiledb_cloud/g'

# A couple files were getting away with using `tiledb.cloud.…` but only `import tiledb`.
# That now breaks, because they're referencing `tiledb_cloud` without importing it.
# Here we patch them, injecting `import tiledb_cloud` under `import tiledb`.
paths=(
  src/tiledb_cloud/soma/ingest.py
  src/tiledb_cloud/asset.py
)
for f in "${paths[@]}"; do
  sed -i '/^import tiledb$/a import tiledb_cloud' "$f"
done
