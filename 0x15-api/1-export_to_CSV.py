#!/usr/bin/python3
"""extend your Python script to export data in the CSV format."""

import csv
import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    userName = user.json().get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, lineterminator='\n')
        for todo in todos.json():
            if todo.get('userId') == int(userId):
                write.writerow([userId, userName, str(todo.get('compcleted')),
                                todo.get('title')])
