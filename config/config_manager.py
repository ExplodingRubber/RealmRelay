import json

from core.paths import get_config_file


DEFAULT_CONFIG = {
    "setup_complete": False,
    "server_locations": [],
    "installed_games": []
}


def load_config():
    config_file = get_config_file()

    if not config_file.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(config_file, "r") as file:
        return json.load(file)


def save_config(config):
    config_file = get_config_file()

    config_file.parent.mkdir(parents=True, exist_ok=True)

    with open(config_file, "w") as file:
        json.dump(config, file, indent=4)