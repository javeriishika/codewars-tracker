import requests
import json
import os

USERNAME = "javeriishika"

KATA_URL = (
    f"https://www.codewars.com/api/v1/users/"
    f"{USERNAME}/code-challenges/completed"
)

response = requests.get(KATA_URL)

response.raise_for_status()

data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/completed_katas.json", "w") as file:
    json.dump(data, file, indent=4)

print("Completed katas saved.")