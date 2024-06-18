#!/usr/bin/python3
''' 1-top_ten.py '''


import requests


def top_ten(subreddit):
    '''
         1. Top Ten
    '''
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
