import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG = {
    "proxies": [],
    "vpn_commands": []
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        save_config(DEFAULT_CONFIG, config_path)
        return DEFAULT_CONFIG
    with open(path, "r") as f:
        return json.load(f)

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)