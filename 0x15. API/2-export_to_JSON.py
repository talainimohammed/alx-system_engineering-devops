#!/usr/bin/python3

"""
Author : TALAINI
Python script that, using a REST API, for a given employee ID
and export to csv
"""

from requests import get
from sys import argv
import json


def exportData():
    resp = get('https://jsonplaceholder.typicode.com/todos/')
    todolist = resp.json()

    resp2 = get('https://jsonplaceholder.typicode.com/users')
    employeelist = resp2.json()
    for i in employeelist:
        if i.get('id') == int(argv[1]):
            employee = i.get('username')

    line = []

    for i in todolist:
        dict = {}
        if i['userId'] == int(argv[1]):
            dict['username'] = employee
            dict['task'] = i['title']
            dict['completed'] = i['completed']
            line.append(dict)

    export_dict = {}
    export_dict[int(argv[1])] = line
    json_obj = json.dumps(export_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)


if __name__ == "__main__":
    exportData()
