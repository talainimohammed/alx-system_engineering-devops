#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """queries the Reddit API and returns a list containing the titles"""

    resp = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        headers={"User-Agent": "MyPythonScript"},
                        params={"count": count, "after": after},
                        allow_redirects=False)
    if resp.status_code >= 400:
        return None

    full_hotlist = hot_list + [child.get("data").get("title")
                               for child in resp.json().get("data")
                               .get("children")]
    page_info = resp.json()
    if not page_info.get("data").get("after"):
        return full_hotlist

    return recurse(subreddit, full_hotlist, page_info.get("data").get("count"),
                   page_info.get("data").get("after"))
