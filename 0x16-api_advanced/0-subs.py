#!/usr/bin/python3
"""number of subscribers."""

import requests
import json

def number_of_subscribers(subreddit):
    API = "https://www.reddit.com/r"
    
    resp = requests.get('{}/{}/about.json'.format(API, subreddit))
    if (resp.status_code == 404):
        return (0)
    for item in resp.data:
        return (item.subscribers)
