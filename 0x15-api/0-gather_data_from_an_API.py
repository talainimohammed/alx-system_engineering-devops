#!/usr/bin/python3

"""
Author : TALAINI
Python script that, using a REST API, for a given employee ID
"""

from requests import get
from sys import argv


def getData():
    resp = get('https://jsonplaceholder.typicode.com/todos/')
    todolist = resp.json()
    completed = 0
    total = 0
    tasks = []
    resp2 = get('https://jsonplaceholder.typicode.com/users')
    employeelist = resp2.json()

    for i in employeelist:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in todolist:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))


if __name__ == "__main__":
    getData()
