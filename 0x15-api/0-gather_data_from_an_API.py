#!/usr/bin/python3
"""This script , using this REST API, for
    a given employee ID, returns information
    about his/her TODO list progress.
    """

import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()
    userName = user.get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    numberOfTaskDone = 0
    totalNumberOfTasks = 0

    for todo in todos:
        if todo.get('userId') == int(userId):
            totalNumberOfTasks += 1
            if todo.get('completed'):
                numberOfTaskDone += 1

    print("Employee {} is done with tasks({}/{}:"
          .format(userName, numberOfTaskDone, totalNumberOfTasks))
    print('\n'.join(["\t " + todo.get('title') for todo in todos
          if todo.get('userId') == int(userId) and todo.get('completed')]))
