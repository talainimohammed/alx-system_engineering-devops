#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first
 10"""

import requests


def top_ten(subreddit):
    """returns the top 10 hot posts
    of the subreddit"""
    resp = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "MyPythonScript"},
                        allow_redirects=False)
    if resp.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in resp.json().get("data").get("children")]
