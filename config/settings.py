import json
from pathlib import Path


CONFIG_FILE = Path(__file__).parent / "config.json"


DEFAULT_CONFIG = {
    "agent_name": "RealmRelay Agent",
    "version": "0.0.51",
    "api_host": "0.0.0.0",
    "api_port": 42069
}


def load_config():
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as file:
            json.dump(DEFAULT_CONFIG, file, indent=4)

        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


config = load_config()


APP_NAME = config.get("agent_name", DEFAULT_CONFIG["agent_name"])
APP_VERSION = config.get("version", DEFAULT_CONFIG["version"])

API_HOST = config.get("api_host", DEFAULT_CONFIG["api_host"])
API_PORT = config.get("api_port", DEFAULT_CONFIG["api_port"])