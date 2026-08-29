# Reproducibility standard

**Research ID:** `R-005`

The goal of this repository is not to maximize benchmark numbers. The goal is to make a published number understandable and repeatable.

## Minimum environment record

Every measured benchmark should include:

- measurement date in UTC;
- NeuroSK version;
- model identifier or model revision;
- input dimensions;
- Windows edition/version/build;
- GPU model, VRAM, and driver version;
- CPU model;
- RAM capacity and relevant memory configuration;
- display/game resolution when the measurement depends on capture dimensions;
- runtime/backend versions;
- power mode / laptop power state when relevant.

## Run protocol

1. Reboot or document the system state before testing.
2. Record all software versions before the run.
3. Use a fixed warm-up period.
4. Collect enough samples for a distribution, not a single observation.
5. Publish the aggregation method with the result.
6. Keep raw measurements when possible.
7. Re-run after major driver/runtime changes rather than silently mixing environments.

## Recommended statistics

For latency-like measurements:

- sample count;
- median;
- p95;
- p99 when the sample count justifies it;
- minimum and maximum as diagnostic values, not headline metrics.

For throughput/FPS-like measurements:

- sample count or timed interval;
- median/average as defined by the methodology;
- p1 or low-percentile behavior when available;
- explicit distinction between inference throughput and full end-to-end application rate.

## Invalid evidence

Do not publish a benchmark row as measured if it is based on:

- a single visual estimate;
- a copied value from another product;
- a theoretical GPU specification;
- an unversioned screenshot;
- a value produced under unknown power/driver settings;
- a guessed or interpolated number.
