# RTX 50-series validation reference

**Research ID:** `R-004`  
**Status:** Reference scaffold — measured benchmark dataset not yet published

NeuroSK publicly targets modern Windows systems and includes RTX 50-series support in its current product requirements. This repository does not publish synthetic performance numbers before a reproducible benchmark run is available.

## Planned validation matrix

For each tested RTX 50-series GPU, record:

- exact GPU model;
- NVIDIA driver version;
- Windows version and build;
- NeuroSK version;
- model/input dimensions;
- runtime/backend version;
- TensorRT/CUDA-related environment information when applicable;
- warm-up duration;
- number of samples;
- median, p95, and minimum/maximum observations when meaningful;
- GPU utilization and VRAM observations where reproducible.

Use [`../data/gpu-benchmark-template.csv`](../data/gpu-benchmark-template.csv) for measured runs.

## Publication rule

A GPU row must remain unpublished until a real measurement record exists. `0`, `N/A`, guessed FPS, or copied marketing values are not valid benchmark results.
