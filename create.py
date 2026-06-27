import json

new_person = {
    "name": {"first": "Juan", "last": "Dela Cruz"},
    "birth": {"place": "Manila", "date": "1990-05-15"},
    "personal": {"age": 36, "gender": "male", "active": True, "verified": False},
    "address": {
        "street": "123 Main St",
        "city": "Manila",
        "province": "Metro Manila",
        "zipCode": "1000",
        "country": "Philippines",
    },
    "contact": {"phone": "09123456789", "email": "juan.delacruz@gmail.com"},
}

with open("data.json", "w") as f:
    json.dump(new_person, f, indent=2)
