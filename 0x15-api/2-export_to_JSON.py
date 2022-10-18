#!/usr/bin/python3
"""extend your Python script to export data in the json format."""

if __name__ == '__main__':

    import csv
    import json
    import requests

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    userName = user.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    toArr = []
    toUser = {}

    for todo in todos.json():
        if todo.get('userId') == int(userId):
            toDict = {"task": todo.get("title"),
                      "completed": todo.get('completed'),
                      "username": userName}
            toArr.append(toDict)
    toUser[userId] = toArr

    filename = userId + '.json'
    with open(filename, mode="w") as f:
        json.dump(toUser, f)
