import json
import os

def read_json():
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as file:
            json.dump([], file)
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file)