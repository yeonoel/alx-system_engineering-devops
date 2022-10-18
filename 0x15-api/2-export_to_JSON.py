#!/usr/bin/python3
"""extend your Python script to export data in the json format."""

import sys
import requests
import csv
import json


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()

    userName = user.get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    toArr = []
    toUser = {}

    for todo in todos:
        if todo.get('userId') == int(userId):
            toDict = {"task": todo.get("title"),
                      "completed": todo.get('completed'),
                      "username": userName}
            toArr.append(toDict)
    toUser[userId] = toArr

    filename = userId + '.json'
    with open(filename, mode="w") as f:
        json.dump(toUser, f)
