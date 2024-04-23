#!/usr/bin/python3
"""  A Python script to export data in the JSON format using Task 0. """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(url + "/todos")

    todos = res.json()
    username = requests.get(url).json().get("username")
    filename = "{}.json".format(argv[1])
    tasks = {}
    _list = []
    for todo in todos:
        _list.append({'task': todo.get("title"), 'completed':
                      todo.get("completed"), 'username': username})
    tasks[argv[1]] = _list
    with open(filename, 'w') as file:
        json.dump(tasks, file)
