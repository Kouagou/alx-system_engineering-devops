#!/usr/bin/python3
""" Querying the Reddit API and returning the number of subscribers. """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        return 0
    except requests.RequestException as e:
        return 0
