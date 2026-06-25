import json


def load_data():
    with open("data.json", "r") as f:
        return json.load(f)


data = load_data()


print(json.dumps(data, indent=2))
