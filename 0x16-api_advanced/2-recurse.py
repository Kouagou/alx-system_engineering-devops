#!/usr/bin/python3
"""
Quering the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ A recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.
    """
    global after
    headers = {'User-Agent': 'linux:0x16.api.advanced'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = response.json().get("data").get("children")
        for title_ in titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
