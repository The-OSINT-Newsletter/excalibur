import requests
import re
from utils.colors import bcolors

def get_profile(mastodon_url):
    if not mastodon_url:
        return {"error": f"{bcolors.FAIL}No Mastodon URL found.{bcolors.ENDC}"}

    domain = mastodon_url.split('/')[2]
    username = mastodon_url.split('@')[-1]
    api_url = f"https://{domain}/api/v1/accounts/lookup?acct={username}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return {
            "display_name": data.get("display_name", "No display name available"),
            "note": strip_html_tags(data.get("note", "No bio available")),
            "url": data.get("url", "No URL available"),
            "avatar": data.get("avatar", "No avatar available"),
            "additional_links": get_additional_links(data.get("fields", [])),
            "match": True
        }
    return {"match": False}

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def get_additional_links(fields):
    additional_links = []
    for field in fields:
        link = field.get("value", "")
        if link and not any(social_link in link for social_link in ["twitter.com", "medium.com"]):
            urls = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', link)
            for url in urls:
                additional_links.append(url)
    return additional_links

def print_profile(profile_info):
    if profile_info.get("match"):
        print(f"{bcolors.OKBLUE}Mastodon URL: {profile_info['url']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Name: {profile_info['display_name']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Bio: {profile_info['note']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Avatar URL: {profile_info['avatar']}{bcolors.ENDC}")
        additional_links = profile_info.get("additional_links", [])
        if additional_links:
            print(f"{bcolors.OKBLUE}Additional Links: {', '.join(additional_links)}{bcolors.ENDC}")
    elif "error" in profile_info:
        print(profile_info["error"])
    else:
        print(f"{bcolors.WARNING}No Mastodon profile found.{bcolors.ENDC}")
