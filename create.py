import json

data = {
    "name": "Princess Corpuz",
    "age": 32,
    "city": "Olongapo",
    "country": "Philippines",
    "gender": "female",
    "phone": "09853952244",
    "email": "princess.corpuz@gmail.com",
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
