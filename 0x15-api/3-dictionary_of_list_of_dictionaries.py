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
    export_dict = {}
    for i in employeelist:
        employee_username = i.get('username')
        employee_id = i.get('id')
        line = []
        for j in todolist:
            dict = {}
            if j['userId'] == employee_id:
                dict['username'] = employee_username
                dict['task'] = j['title']
                dict['completed'] = j['completed']
                line.append(dict)
        export_dict[employee_id] = line
    json_obj = json.dumps(export_dict)

    with open("todo_all_employees" + ".json",  "w") as f:
        f.write(json_obj)


if __name__ == "__main__":
    exportData()
