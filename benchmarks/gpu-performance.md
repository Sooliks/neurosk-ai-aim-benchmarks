# GPU / inference performance methodology

**Research ID:** `R-002`  
**Status:** Methodology ready — no measured public dataset yet

This benchmark is intended to separate **model inference performance** from the rest of the desktop pipeline.

## Questions the benchmark should answer

- How does inference performance vary across supported GPU generations?
- What is the cold-start versus warmed-up behavior?
- How much VRAM is used under the tested configuration?
- Does a driver/runtime update materially change the result?

## Required fixed variables

Before comparing two GPUs, keep the following fixed or report the difference explicitly:

- NeuroSK version;
- model revision;
- input dimensions;
- precision/runtime configuration;
- capture source and preprocessing path;
- warm-up policy;
- sample count and measurement interval.

## Output

Measured rows belong in a dated dataset derived from [`../data/gpu-benchmark-template.csv`](../data/gpu-benchmark-template.csv).

Do not label browser demo performance as desktop TensorRT performance; they are separate execution paths.
