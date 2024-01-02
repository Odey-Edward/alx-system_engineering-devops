#!/usr/bin/python3
"""
a Python script that, uses a REST API, for a given employee ID,
export information about his/her TODO list progress in json format
to a file"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(url).json()
    todos = requests.get(todo_url).json()

    value = []
    info = {}

    for user in users:
        for data in todos:
            if user.get('id') == data.get('userId'):
                value.append({"username": user.get('username'),
                             "task": data.get('title'),
                              "completed": data.get('completed')})
        info[user.get('id')] = value
        value = []

    with open('todo_all_employees.json', 'w') as file:
        json.dump(info, file)
