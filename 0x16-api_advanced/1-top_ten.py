#!/usr/bin/python3
"""Function that print hot posts on a given subreddit"""
import requests


def top_ten(subreddit):
    """Printing the titles of the 10 hot posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(ch.get("data").get("title")) for ch in res.get("children")]
