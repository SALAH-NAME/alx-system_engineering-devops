#!/usr/bin/python3
'''0-subs.py'''


import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.1.0 (by /u/vagrant)"}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        res = r.json().get("data")
        subs = res.get("subscribers")
        return subs
    else:
        return 0
