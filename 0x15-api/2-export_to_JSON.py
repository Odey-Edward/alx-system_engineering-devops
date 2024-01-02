#!/usr/bin/python3
"""
a Python script that, uses a REST API, for a given employee ID,
export information about his/her TODO list progress in json format
to a file"""
import json
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
                {"task": data.get('title'), "completed": data.get('completed'),
                    "username": user.get('username')})

    info = {data.get('userId'): value}

    with open(str(id) + '.json', 'w') as file:
        json.dump(info, file)
