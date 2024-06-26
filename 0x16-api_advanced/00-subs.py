#!/usr/bin/python3
""" Quering the Reddit API and returns the number of subscribers. """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        print("OK")
        datas = response.json()
        return datas['data']['subscribers']
    else:
        print("Maudiaaa")
        return 0
