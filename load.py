import json


def load():
    with open("config.json") as f:
        config = json.load(f)
    if len(config) == 0:
        return "Setup required"
    return config
