import json


data = {
    "name": {"title": "Mr", "first": "Juan", "last": "Dela Cruz"},
    "dob": {"date": "1990-05-15T00:00:00Z", "age": 36},
    "location": {
        "city": "Manila",
        "region": "Metro Manila",
        "country": "Philippines",
        "zipcode": "1000",
    },
    "gender": "male",
    "phone": "09123456789",
    "email": "juan.delacruz@gmail.com",
    "registered": {"date": "2025-01-15T10:30:00Z", "age": 1},
    "active": True,
    "verified": False,
}


with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
