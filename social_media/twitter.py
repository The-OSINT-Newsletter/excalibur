import requests
from utils.colors import bcolors

def check_archived(username):
    url = f"https://archive.org/wayback/available?url=twitter.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        archived_url = data.get("archived_snapshots", {}).get("closest", {}).get("url", "No archive available")
        if archived_url != "No archive available":
            return f"{bcolors.OKGREEN}Twitter archive available: {archived_url}{bcolors.ENDC}"
        else:
            return f"{bcolors.WARNING}No Twitter archive available.{bcolors.ENDC}"
    return f"{bcolors.FAIL}Failed to check Twitter archive.{bcolors.ENDC}"
