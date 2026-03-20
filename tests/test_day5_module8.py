import pytest
import os
import json

def test_day5_files_exist():
    required_files = [
        "artifacts/day5/yang/ietf-interfaces.yang",
        "artifacts/day5/yang/pyang_tree.txt",
        "artifacts/day5/webex/room_create.json",
        "artifacts/day5/pt/serviceTicket.txt"
    ]
    for f in required_files:
        assert os.path.exists(f), f"Missing required file: {f}"

def test_day5_summary_validation():
    assert os.path.exists("summary.json")
    with open("summary.json", "r") as f:
        summary = json.load(f)
    
    assert summary["schema_version"] == "5.0"
    assert summary["checks"]["yang_tree_ok"] is True
    assert summary["checks"]["webex_room_hash_ok"] is True
    assert summary["checks"]["pt_external_access_ok"] is True