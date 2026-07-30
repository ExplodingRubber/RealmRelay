from pathlib import Path


def get_application_directory():
    return Path(__file__).resolve().parent.parent


def get_data_directory():
    return get_application_directory() / "data"


def get_config_file():
    return get_data_directory() / "config.json"