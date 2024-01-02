#!/usr/bin/python3
"""
a Python script that, uses a REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(url + str(id)).json()
    todos = requests.get(todo_url).json()

    doneTask = []
    requiredTodo = []
    totalTask = 0
    numDoneTask = 0

    for todo in todos:
        if todo.get("userId") == id:
            requiredTodo.append(todo)
            totalTask += 1

    for todo in requiredTodo:
        if todo.get("completed") is True:
            doneTask.append(todo.get("title"))
            numDoneTask += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user.get("name"), numDoneTask, totalTask))
    for task in doneTask:
        print('\t {}'.format(task))
