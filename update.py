import json

with open("data.json", "r") as f:
    data = json.load(f)

data["person"][0]["email"] = "juan.delacruz@yahoo.com"
data["person"][0]["location"]["city"] = "Subic"
data["person"][0]["phone"] = "09991234567"


data["person"][1]["email"] = "maria.santos@gmail.com"
data["person"][1]["location"]["city"] = "Davao City"
data["person"][1]["phone"] = "09998765432"

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
