#!/usr/bin/python3
"""  A Python script to export data in the CSV format using Task 0. """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(url + "/todos")

    todos = res.json()
    username = requests.get(url).json().get("username")
    filename = "{}.csv".format(argv[1])
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], username, todo.get("completed"),
                            todo.get("title")])
