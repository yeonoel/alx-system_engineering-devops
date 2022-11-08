#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
   containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list containing the titles of all hot articles."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ypn)"}

    params = {
            "after": after,
            "count": count,
            "limite": 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if (response.status_code >= 300):
        return (None)

    resp = response.json()['data']['children']
    hot_list.append([print(elem.get('data').get('title')) for elem in resp])
    count += response.json().get('data').get('dist')
    after = response.json().get('data').get('after')

    if (after is not None):
        return (recurse(subreddit, hot_list, after, count))
    return hot_list
