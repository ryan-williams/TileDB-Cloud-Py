# Changes

## Next (2024-09-23)

---

New features:

- Assets of a namespace can be listed in a paged fashion (gh-642).

## Next (YYYY-MM-DD)

New features:

- Add a tiledb_cloud.asset module with functions that allow management of
  assets of any type. This module is exported from tiledb_cloud (gh-566,
  gh-577).

Bug fixes:

- Enable ingestion of multi-band geospatial raster data (gh-609).
- Ensure that boolean recursive parameters in tiledb_cloud.asset and
  tiledb_cloud.groups are converted to "true" or "false" before server requests
  are made (gh-605).
