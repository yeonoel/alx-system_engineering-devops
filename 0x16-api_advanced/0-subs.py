#!/usr/bin/python3
"""number of subscribers."""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers . """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ypn"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if (response.status_code >= 300):
        return (0)

    results = response.json().get('data')
    return (results.get('subscribers'))
