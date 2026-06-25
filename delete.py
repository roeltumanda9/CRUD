import json


with open("data.json", "r") as f:
    data = json.load(f)


del data["phone"]


with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
