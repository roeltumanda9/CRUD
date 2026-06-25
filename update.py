import json


with open("data.json", "r") as f:
    data = json.load(f)


data["age"] = 33
data["city"] = "Subic"
data["phone"] = "09991234567"


with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
