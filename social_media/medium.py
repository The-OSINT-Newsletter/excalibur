import requests
import re
from utils.colors import bcolors

headers = {
    'authority': 'medium.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'lite',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_profile(username):
    url = 'https://medium.com/_/graphql'
    payload = [{"operationName":"UserAboutQuery","variables":{"id":None,"username":username},"query":"query UserAboutQuery($username: ID, $id: ID) { userResult(username: $username, id: $id) { __typename ... on User { id name username bio imageId linkedAccounts { mastodon { domain username } } } } }"}]

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        user_data = data[0].get('data', {}).get('userResult', {})
        if user_data and user_data.get('name', None):
            mastodon_account = user_data.get('linkedAccounts', {}).get('mastodon', {})
            mastodon_url = f"https://{mastodon_account.get('domain', '')}/@{mastodon_account.get('username', '')}" if mastodon_account else ''
            return {
                "name": user_data.get('name', 'No name available'),
                "bio": user_data.get('bio', 'No bio available'),
                "avatarUrl": f"https://miro.medium.com/v2/resize:fill:176:176/{user_data.get('imageId', 'No image ID available')}",
                "mediumUrl": f"https://medium.com/@{username}",
                "mastodonUrl": mastodon_url,
                "match": True
            }
        else:
            return {"match": False}
    return {"error": f"{bcolors.FAIL}Failed to fetch Medium profile.{bcolors.ENDC}"}

def print_profile(profile_info):
    if profile_info.get("match"):
        print(f"{bcolors.OKBLUE}Name: {profile_info['name']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Bio: {strip_html_tags(profile_info['bio'])}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Avatar URL: {profile_info['avatarUrl']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}URL: {profile_info['mediumUrl']}{bcolors.ENDC}")
    elif "error" in profile_info:
        print(profile_info["error"])
    else:
        print(f"{bcolors.WARNING}No exact username match found on Medium.{bcolors.ENDC}")

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
