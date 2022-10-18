#!/usr/bin/python3
"""extend your Python script to export data in the CSV format."""

import sys
import requests
import csv


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()
    userName = user.get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, lineterminator='\n')
        for todo in todos:
            if todo.get('userId') == int(userId):
                write.writerow([userId, userName, str(todo.get('compcleted')),
                                todo.get('title')])
