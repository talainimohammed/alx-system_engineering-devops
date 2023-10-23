#!/usr/bin/python3

"""
Author : TALAINI
Python script that, using a REST API, for a given employee ID
and export to csv
"""

from requests import get
from sys import argv
import csv


def exportData():
    resp = get('https://jsonplaceholder.typicode.com/todos/')
    todolist = resp.json()

    resp2 = get('https://jsonplaceholder.typicode.com/users')
    employeelist = resp2.json()
    for i in employeelist:
        if i.get('id') == int(argv[1]):
            employee = i.get('username')

    with open(argv[1] + '.csv', 'w', newline='') as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in todolist:
            line = []
            if i['userId'] == int(argv[1]):
                line.append(i['userId'])
                line.append(employee)
                line.append(i['completed'])
                line.append(i['title'])

                w.writerow(line)


if __name__ == "__main__":
    exportData()
