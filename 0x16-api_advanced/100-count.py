#!/usr/bin/python3
''' 100-count.py '''


import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=Counter()):
    '''
         3. Count it!
    '''
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]
    for title in titles:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                word_count[word] += 1
    if data['after']:
        return count_words(subreddit, word_list, data['after'], word_count)
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print('{}: {}'.format(word, count))
    return
