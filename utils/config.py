import json, sys

# Load config and data

if len(sys.argv) > 1 and sys.argv[1] == "dev":
    dev = True
else:
    dev = False

# Load config
def load():
    with open("CONFIG.json" if not dev else "devCONFIG.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

# Update config
def update():
    with open("CONFIG.json" if not dev else "devCONFIG.json", "w", encoding="utf-8") as f:
        json.dump(CONFIG, f, ensure_ascii=False, indent=4)


CONFIG = load()
