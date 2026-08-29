#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read_csv(path: str) -> list[dict[str, str]]:
    file_path = ROOT / path
    if not file_path.exists():
        fail(f"missing required file: {path}")
        return []
    with file_path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def require_headers(path: str, expected: list[str]) -> list[dict[str, str]]:
    file_path = ROOT / path
    if not file_path.exists():
        fail(f"missing required file: {path}")
        return []
    with file_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        actual = reader.fieldnames or []
        if actual != expected:
            fail(f"{path}: unexpected headers: {actual!r}")
        return list(reader)


def validate_mouse_methods() -> None:
    expected_headers = [
        "method", "class", "basic", "advanced", "windows", "hardware_required",
        "status", "secure_boot_note", "canonical_reference", "last_verified",
    ]
    rows = require_headers("data/mouse-output-methods.csv", expected_headers)
    if len(rows) != 10:
        fail(f"data/mouse-output-methods.csv: expected 10 methods, got {len(rows)}")

    names = [row.get("method", "") for row in rows]
    if len(names) != len(set(names)):
        fail("data/mouse-output-methods.csv: duplicate method names")

    for row in rows:
        if row.get("basic") not in {"true", "false"}:
            fail(f"invalid basic flag for {row.get('method')}")
        if row.get("advanced") not in {"true", "false"}:
            fail(f"invalid advanced flag for {row.get('method')}")
        if row.get("hardware_required") not in {"true", "false"}:
            fail(f"invalid hardware_required flag for {row.get('method')}")
        if row.get("canonical_reference") != "https://neurosk.pro/en/mouse-drivers":
            fail(f"unexpected canonical reference for {row.get('method')}")


def validate_registry() -> None:
    rows = read_csv("data/research-registry.csv")
    ids = [row.get("id", "") for row in rows]
    if not ids or len(ids) != len(set(ids)):
        fail("data/research-registry.csv: IDs must be present and unique")
    for row in rows:
        primary = row.get("primary_file", "")
        if primary and not (ROOT / primary).exists():
            fail(f"research registry references missing primary file: {primary}")
        data_file = row.get("data_file", "")
        if data_file and not (ROOT / data_file).exists():
            fail(f"research registry references missing data file: {data_file}")


def validate_benchmark_templates() -> None:
    for path in ["data/gpu-benchmark-template.csv", "data/latency-benchmark-template.csv"]:
        file_path = ROOT / path
        lines = file_path.read_text(encoding="utf-8").splitlines()
        if len(lines) != 1:
            fail(f"{path}: template must remain header-only until measured evidence is published")


def validate_readme() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required = [
        "https://neurosk.pro/en/mouse-drivers",
        "https://neurosk.pro/en/test-ai",
        "CITATION.cff",
        "first-party technical material",
        "no fabricated performance numbers",
    ]
    for item in required:
        if item not in text:
            fail(f"README.md missing required integrity marker: {item}")


def validate_private_content_guardrails() -> None:
    forbidden_names = {".env", "id_rsa", "license.key", "secrets.json"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.name.lower() in forbidden_names:
            fail(f"forbidden private/secrets-like file present: {path.relative_to(ROOT)}")


def main() -> int:
    validate_mouse_methods()
    validate_registry()
    validate_benchmark_templates()
    validate_readme()
    validate_private_content_guardrails()

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1

    print("NeuroSK research repository validation passed.")
    print("- mouse output methods: 10")
    print("- research registry: valid")
    print("- benchmark templates: evidence-safe")
    print("- citation/integrity markers: present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
