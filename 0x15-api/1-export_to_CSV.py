#!/usr/bin/python3
"""
a Python script that, uses a REST API, for a given employee ID,
export information about his/her TODO list progress to an
csv file"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(url + str(id)).json()
    todos = requests.get(todo_url).json()

    value = []
    requiredTodo = []

    for todo in todos:
        if todo.get("userId") == id:
            requiredTodo.append(todo)

    for data in requiredTodo:
        value.append(
                [data.get('userId'), user.get('username'),
                    data.get('completed'), data.get('title')])

    with open(str(id) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(value)
