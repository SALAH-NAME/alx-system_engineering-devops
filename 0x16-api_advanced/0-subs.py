#!/usr/bin/python3
'''0-subs.py'''


import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'
    user_agent = '0x16-api_advanced:project:v0.1.0 (by someone_unknown)'
    r = requests.get(url.format(subreddit),
                     headers={'User-Agent': user_agent}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
