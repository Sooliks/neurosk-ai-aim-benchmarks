# Benchmark data schema

The CSV templates in this directory are intentionally header-only until measured evidence exists.

## General rules

- `run_id` must be unique and stable.
- Dates use ISO 8601 / UTC where possible.
- Units are encoded in column names (`_ms`, `_mb`, `_gb`).
- Empty means **not measured / not applicable**. Do not use `0` as a substitute for missing data.
- `evidence_path` should point to raw data, logs, or a versioned artifact included in a future benchmark release.

## Versioning

Changing a column name is a schema change. Prefer adding a new column to silently changing the meaning of an existing one.
