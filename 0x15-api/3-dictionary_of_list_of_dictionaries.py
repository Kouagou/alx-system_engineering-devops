#!/usr/bin/python3
"""  A Python script to export data in the JSON format using Task 0. """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    tasks = {}
    for user in users:
        todos = requests.get(url + "/{}/todos".format(user.get('id'))).json()
        _list = []
        for todo in todos:
            _list.append({'task': todo.get("title"),
                          'completed': todo.get("completed"),
                          'username': user.get('username')})
        tasks[user.get('id')] = _list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(tasks, file)
