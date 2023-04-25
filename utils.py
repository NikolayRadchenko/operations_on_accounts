import json


def read_json():
    with open("./data/operations.json", encoding="utf-8") as f:
        return json.load(f)
