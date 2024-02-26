import requests
from utils.colors import bcolors

def get_profile(username):
    url = 'https://www.producthunt.com/frontend/graphql'
    payload = {
        'query': '''
            query ProfileLayoutQuery($username: String!) {
                profile: user(username: $username) {
                    id
                    name
                    headline
                    avatarUrl
                    twitterUsername
                    __typename
                }
            }
        ''',
        'variables': {
            'username': username
        }
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        profile = data.get('data', {}).get('profile', {})
        if profile and profile.get('twitterUsername', '').lower() == username.lower():
            return {
                "name": profile.get('name', 'No name available'),
                "headline": profile.get('headline', 'No headline available'),
                "avatarUrl": profile.get('avatarUrl', 'No avatar URL available'),
                "productHuntUrl": f"https://www.producthunt.com/@{username}",
                "match": True
            }
        else:
            return {"match": False}
    return {"error": f"{bcolors.FAIL}Failed to fetch Product Hunt profile.{bcolors.ENDC}"}

def print_profile(profile_info):
    if profile_info.get("match"):
        print(f"{bcolors.OKBLUE}Name: {profile_info['name']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Headline: {profile_info['headline']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Avatar URL: {profile_info['avatarUrl']}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}URL: {profile_info['productHuntUrl']}{bcolors.ENDC}")
    elif "error" in profile_info:
        print(profile_info["error"])
    else:
        print(f"{bcolors.FAIL}No Product Hunt account found.{bcolors.ENDC}")
