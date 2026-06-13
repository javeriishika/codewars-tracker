import json

with open("data/profile.json") as file:
    profile = json.load(file)

with open("data/completed_katas.json") as file:
    katas = json.load(file)

username = profile["username"]

rank = profile["ranks"]["overall"]["name"]

honor = profile["honor"]

total_solved = katas["totalItems"]

readme_content = f"""
# Codewars Tracker

## Profile

- Username: {username}
- Rank: {rank}
- Honor: {honor}
- Total Solved Kata: {total_solved}

## About

This repository automatically tracks my Codewars progress.

### Technologies Used

- Python
- REST APIs
- GitHub Actions
- JSON

Last Updated Automatically
"""

with open("README.md", "w") as file:
    file.write(readme_content)

print("README generated.")