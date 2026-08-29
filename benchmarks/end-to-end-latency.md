# End-to-end latency methodology

**Research ID:** `R-003`  
**Status:** Methodology ready — no measured public dataset yet

End-to-end latency must be defined before it is measured. A useful NeuroSK measurement should identify the start and end event explicitly rather than publishing one generic "latency" number.

## Suggested stages

1. frame/capture availability;
2. preprocessing complete;
3. inference complete;
4. post-processing / target decision complete;
5. mouse-output command emitted;
6. output transport acknowledged or observed, when measurable.

## Recommended published metrics

- `capture_to_inference_ms`
- `inference_ms`
- `postprocess_ms`
- `decision_to_output_ms`
- `capture_to_output_ms`

If a stage cannot be measured reliably, leave it blank and document why. Do not derive a fake total from incompatible clocks.

Use [`../data/latency-benchmark-template.csv`](../data/latency-benchmark-template.csv).
