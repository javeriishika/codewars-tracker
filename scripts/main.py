import subprocess

subprocess.run(
    ["python", "scripts/fetch_profile.py"]
)

subprocess.run(
    ["python", "scripts/fetch_katas.py"]
)

subprocess.run(
    ["python", "scripts/generate_readme.py"]
)