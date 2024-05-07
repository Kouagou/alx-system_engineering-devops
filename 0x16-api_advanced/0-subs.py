#!/usr/bin/python3
""" Quering the Reddit API and returns the number of subscribers. """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-agent': 'linux:0x16.api.advanced'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    datas = response.json()

    try:
        return datas.get("subscribers")
    except Exception:
        return 0
