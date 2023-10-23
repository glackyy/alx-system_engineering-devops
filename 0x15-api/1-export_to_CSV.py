#!/usr/bin/python3
"""Returning to-do list information for a given employee id"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [wr.writerow(
            [user_id, username, td.get("completed"), td.get("title")]
        ) for td in todos]
