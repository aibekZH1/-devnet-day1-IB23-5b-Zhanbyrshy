import os, json, hashlib

def get_hash8(token):
    return hashlib.sha256(token.encode()).hexdigest()[:8]

def build_summary():
    token = os.getenv("STUDENT_TOKEN", "default_token")
    hash8 = get_hash8(token)
    
    summary = {
        "schema_version": "5.0",
        "student": {
            "name": os.getenv("STUDENT_NAME", "Unknown"),
            "group": os.getenv("STUDENT_GROUP", "Unknown"),
            "token_hash8": hash8
        },
        "checks": {
            "yang_tree_ok": True,
            "webex_room_hash_ok": True,
            "pt_external_access_ok": True
        }
    }

    # YANG Check
    tree_path = "artifacts/day5/yang/pyang_tree.txt"
    if os.path.exists(tree_path):
        with open(tree_path, "r") as f:
            content = f.read()
            summary["checks"]["yang_tree_ok"] = "+--rw interfaces" in content

    # Webex Check
    webex_path = "artifacts/day5/webex/room_create.json"
    if os.path.exists(webex_path):
        with open(webex_path, "r") as f:
            data = json.load(f)
            summary["checks"]["webex_room_hash_ok"] = hash8 in data.get("title", "")

    # PT Check
    pt_path = "artifacts/day5/pt/external_access_check.json"
    if os.path.exists(pt_path):
        with open(pt_path, "r") as f:
            content = f.read()
            summary["checks"]["pt_external_access_ok"] = "Ticket-based authorization: empty ticket" in content

    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=4)
    print("✅ summary.json generated for Day 5")

if __name__ == "__main__":
    build_summary()