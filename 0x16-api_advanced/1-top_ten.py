#!/usr/bin/python3

"""
Quering the Reddit API and prints the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """ A function that queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'linux:0x16.api.advanced'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=headers, params=params)
    results = response.json()

    try:
        datas = results.get('data').get('children')

        for i in datas:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
