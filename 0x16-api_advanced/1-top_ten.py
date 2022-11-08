#!/usr/bin/python3
""" Function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10
       hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ypn)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if (response.status_code >= 300):
        print("None")
    else:
        results = response.json().get('data').get('children')

        for elem in results:
            x = elem.get("data").get("title")
            print(x)
