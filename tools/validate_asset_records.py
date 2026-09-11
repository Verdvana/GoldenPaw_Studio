#!/usr/bin/env python3
"""Dependency-free checks for GoldenPaw YAML-like Canon records.

This deliberately validates governance-critical text patterns without requiring a
YAML package. It does not promote, approve, lock, move, or modify any asset.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "templates"}
REQUIRED_METADATA = {
    "asset_id",
    "asset_level",
    "generated_or_real",
    "approval_status",
    "authoritative_for",
    "must_not_define",
}


def keys(text: str) -> set[str]:
    return set(re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", text, re.MULTILINE))


def is_registered_in_manifest(path: Path) -> bool:
    """Accept a sidecar or an entry in an ancestor SOURCE_MANIFEST.md."""
    current = path.parent
    while current != ROOT.parent:
        manifest = current / "SOURCE_MANIFEST.md"
        if manifest.exists():
            text = manifest.read_text(encoding="utf-8")
            try:
                relative = path.relative_to(current).as_posix()
            except ValueError:
                relative = path.name
            candidates = {path.name, relative}
            if relative.startswith("raw/"):
                candidates.add(relative.removeprefix("raw/"))
            if any(f"`{candidate}`" in text for candidate in candidates):
                return True
        if current == ROOT:
            break
        current = current.parent
    return False


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in ROOT.rglob("*.yaml"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == "CANON_MANIFEST.yaml":
            if "lock_status: \"LOCKED\"" in text:
                if not re.search(r"approval_records:\s*\n\s*-", text):
                    errors.append(f"{path}: locked Canon has no approval record")
                if re.search(r"checksum_sha256:\s*\"\"", text):
                    errors.append(f"{path}: locked Canon contains an empty checksum")
        elif path.name.endswith(".metadata.yaml"):
            missing = REQUIRED_METADATA - keys(text)
            if missing:
                errors.append(f"{path}: missing keys {sorted(missing)}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        is_l0_raw = "raw" in path.parts and (
            "source" in path.parts or "source_library" in path.parts
        )
        if is_l0_raw and path.name != ".gitkeep":
            sidecar = path.with_name(path.name + ".metadata.yaml")
            if not sidecar.exists() and not is_registered_in_manifest(path):
                warnings.append(f"{path}: L0 original has no sidecar or SOURCE_MANIFEST.md entry")

    reference_registry = ROOT / "registries" / "reference_sets.yaml"
    if reference_registry.exists():
        text = reference_registry.read_text(encoding="utf-8")
        for relative in re.findall(r'path:\s*"([^"]+)"', text):
            if not (ROOT / relative).is_file():
                errors.append(f"{reference_registry}: missing referenced file {relative}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    print(f"Validation complete: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
