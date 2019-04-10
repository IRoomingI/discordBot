import json

# Load config and data

mode = "prod"

# Load config
def load():
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

# Update config
def update():
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "w", encoding="utf-8") as f:
        json.dump(CONFIG, f, ensure_ascii=False, indent=4)


CONFIG = load()
