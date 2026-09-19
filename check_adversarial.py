"""Compare adversarial output with the expected routing decisions."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
expected = json.loads((ROOT / "fixtures" / "adversarial_expected.json").read_text(encoding="utf-8"))
actual_list = json.loads((ROOT / "output" / "adversarial_decisions.json").read_text(encoding="utf-8"))
actual = {item["lead_id"]: item for item in actual_list}

errors = []
if len(actual_list) != len(expected):
    errors.append(f"count mismatch: expected {len(expected)} got {len(actual_list)}")
extra = set(actual) - set(expected)
missing = set(expected) - set(actual)
if extra:
    errors.append(f"unexpected lead_ids: {sorted(extra)}")
if missing:
    errors.append(f"missing lead_ids: {sorted(missing)}")

mismatches = [
    (lead_id, expected_decision, actual.get(lead_id, {}).get("decision"), actual.get(lead_id, {}).get("reason"))
    for lead_id, expected_decision in expected.items()
    if actual.get(lead_id, {}).get("decision") != expected_decision
]

if mismatches:
    for mismatch in mismatches:
        print(mismatch)
    sys.exit(1)

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print(f"Adversarial check passed: {len(expected)} decisions match")
