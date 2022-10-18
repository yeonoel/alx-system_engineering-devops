#!/usr/bin/python3
"""This script extend your Python script to export data in the JSON format."""

import requests
import sys
import json


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    toAll = {}
    toArr = []
    for user in users:
        taskList = []
        userName = user.get('name')
        for todo in todos:
            if todo.get('userId') == user.get('userId'):
                toDict = {"username": userName,
                          "task": todo.get('title'),
                          "completed": todo.get('completed')}
                toArr.append(toDict)
        toAll[user.id] = toArr

    filename = todo_all_employees.json
    with open(filename, mode="w") as f:
        json.dump(toAll, f)
