# NeuroSK mouse output methods

**Research ID:** `R-001`  
**Snapshot:** `2026-08-29`  
**Status:** Published public reference snapshot

This document mirrors the public NeuroSK mouse-output reference in a stable, citation-friendly format. The canonical product page remains:

- English: https://neurosk.pro/en/mouse-drivers
- Russian: https://neurosk.pro/mouse-drivers

The machine-readable table is [`../data/mouse-output-methods.csv`](../data/mouse-output-methods.csv).

## Classification

NeuroSK currently groups output methods into five practical classes:

1. **Software / vendor interfaces** — e.g. Logitech GHub and Razer RZCONTROL.
2. **Software drivers** — e.g. No name driver, Interception, TT Driver.
3. **Operating-system input** — Windows Input fallback.
4. **Virtual HID** — NeuroSK HID and FakerInput.
5. **Hardware USB HID** — MAKCU and CH9329.

## Important interpretation notes

- `Supported` means the method is publicly documented as available, not that every game or environment is guaranteed to accept it.
- `Beta` and `Beta / MVP` entries can have incomplete per-game validation.
- Secure Boot requirements can differ by method and Windows configuration.
- Hardware HID methods require separate physical hardware.
- Compatibility observations are versioned and should be revalidated after major Windows, vendor-driver, or NeuroSK changes.

## Public snapshot

| Method | Class | Basic | Advanced | Hardware required | Windows | Status |
|---|---|:---:|:---:|:---:|---|---|
| Logitech GHub | Software / vendor interface | Yes | Yes | No | Windows 10 / 11 | Supported |
| No name driver | Software driver | Yes | Yes | No | Windows 10 | Supported |
| Interception | Software driver | No | Yes | No | Windows 10 / 11 | Supported |
| TT Driver | Software driver | No | Yes | No | Windows 10 / 11* | Recommended |
| Windows Input | OS input | No | Yes | No | Windows 10 / 11 | Fallback |
| NeuroSK HID | Virtual HID | No | Yes | No | Windows 10 / 11 x64 | Beta |
| FakerInput | Virtual HID | No | Yes | No | Windows 10 / 11 x64 | Beta |
| Razer Synapse (RZCONTROL) | Vendor interface | No | Yes | No | Windows 10 / 11 | Beta |
| MAKCU (USB HID) | Hardware USB HID | No | Yes | Yes | Windows 10 / 11 x64 | Beta / MVP |
| CH9329 USB HID | Hardware USB HID | No | Yes | Yes | Windows 10 / 11 x64 | Beta / MVP |

`*` Some Windows 11 systems may require additional Secure Boot configuration.

## Citation guidance

When citing a method or compatibility statement, include the snapshot date. This avoids treating a time-sensitive compatibility observation as permanent.
