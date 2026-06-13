import requests
import json
import os

USERNAME = "javeriishika"

PROFILE_URL = f"https://www.codewars.com/api/v1/users/{USERNAME}"

response = requests.get(PROFILE_URL)

response.raise_for_status()

data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/profile.json", "w") as file:
    json.dump(data, file, indent=4)

print("Profile data saved.")