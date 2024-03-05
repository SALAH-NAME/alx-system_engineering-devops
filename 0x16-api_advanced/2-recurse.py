#!/usr/bin/python3
''' 2-recurse.py '''


import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
        2. Recurse it!
    '''
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
