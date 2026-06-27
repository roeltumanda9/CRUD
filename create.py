import json


person1 = {
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

person2 = {
    "name": {"title": "Ms", "first": "Maria", "last": "Santos"},
    "dob": {"date": "1995-08-22T00:00:00Z", "age": 30},
    "location": {
        "city": "Cebu City",
        "region": "Central Visayas",
        "country": "Philippines",
        "zipcode": "6000",
    },
    "gender": "female",
    "phone": "09876543210",
    "email": "maria.santos@yahoo.com",
    "registered": {"date": "2024-06-15T14:20:00Z", "age": 1},
    "active": True,
    "verified": True,
}

data = {"person": [person1, person2]}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
