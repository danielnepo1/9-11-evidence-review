"""Offline structural gate; does not validate historical research conclusions."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "fc84dc8"
HISTORICAL = ["README.md", "NEXT-STEPS.md", "SOURCES.md",
              "docs/01-wtc-engineering-audit-v1.md",
              "docs/02-adversarial-audit-phase1.md",
              "docs/03-phase2a-mfr-verification.md"]
for name in HISTORICAL:
    before = subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)
    assert (ROOT / name).read_bytes() == before, f"historical record changed: {name}"
for directory, ref, names in [
    ("2026-09-19-phase2a", "c28c8ce", HISTORICAL),
    ("2026-09-21-research", "0b6dac3", ["README.md", "NEXT-STEPS.md", "SOURCES.md",
                                            "docs/03-phase2a-mfr-verification.md"]),
]:
    for name in names:
        before = subprocess.check_output(["git", "show", f"{ref}:{name}"], cwd=ROOT)
        assert (ROOT / "sessions" / directory / name).read_bytes() == before, name
for path in ROOT.rglob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))
for path in ROOT.rglob("*.jsonl"):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            json.loads(line)
for name in ("docs/08-reorientation-directed-search.md", "docs/12-b2-eit-timing-crossref.md",
             "docs/prereg/B2-ch5-EIT-timing.md", "REPRODUCIBILITY.md"):
    assert (ROOT / name).is_file(), name
print("PASS: historical bytes, source snapshots, JSON/JSONL and research entry points")
