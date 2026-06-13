import json

with open("data/completed_katas.json") as file:
    data = json.load(file)

print("Total solved:", data["totalItems"])

print("\nFirst Kata:\n")

print(data["data"][0])