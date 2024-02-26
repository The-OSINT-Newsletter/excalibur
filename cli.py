import argparse
from social_media import twitter, product_hunt, medium, mastodon
from utils.colors import bcolors

def print_divider(title=''):
    print(f"\n{bcolors.BOLD}{bcolors.HEADER}{title.center(60, '-')}{bcolors.ENDC}")

def print_ascii_menu():
    print("""
   _____  __________   __   _______  __  _____ 
  / __/ |/_/ ___/ _ | / /  /  _/ _ )/ / / / _ \\
 / _/_>  </ /__/ __ |/ /___/ // _  / /_/ / , _/
/___/_/|_|\___/_/ |_/____/___/____/\____/_/|_|                                    
""")
    print("By: @osintnewsletter")

def main():
    parser = argparse.ArgumentParser(description="Check if a Twitter username is archived and fetch Product Hunt, Medium, and Mastodon profiles.")
    parser.add_argument("--u", type=str, required=True, help="The Twitter username to check")
    args = parser.parse_args()

    print_ascii_menu()

    print_divider("Checking Twitter Archive Status")
    twitter_archive_status = twitter.check_archived(args.u)
    print(twitter_archive_status)

    print_divider("Fetching Product Hunt Profile Info")
    ph_profile_info = product_hunt.get_profile(args.u)
    product_hunt.print_profile(ph_profile_info)

    print_divider("Fetching Medium Profile Info")
    medium_profile_info = medium.get_profile(args.u)
    medium.print_profile(medium_profile_info)

    print_divider("Fetching Mastodon Profile Info")
    mastodon_profile_info = mastodon.get_profile(medium_profile_info.get('mastodonUrl', ''))
    mastodon.print_profile(mastodon_profile_info)

if __name__ == "__main__":
    main()
