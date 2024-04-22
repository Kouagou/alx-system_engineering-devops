#!/usr/bin/python3
""" A Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    res = requests.get(url)

    todos = res.json()

    employe_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1])).json().get("name")
    try:
        number_of_done_tasks = len([todo for todo in todos
                                    if todo.get("completed") is True])
        total_number_of_tasks = len([todo for todo in todos])

        print("Employee {} is done with tasks({}/{}):"
              .format(employe_name, number_of_done_tasks,
                      total_number_of_tasks))
        for todo in todos:
            if todo.get("completed") is True:
                print("\t {}".format(todo.get("title")))
    except IndexError:
        pass
