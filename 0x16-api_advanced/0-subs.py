#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """the number of subscribers"""
    resp = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "MyPythonScript"})
    if resp.status_code >= 300:
        return 0

    return resp.json().get("data").get("subscribers")
