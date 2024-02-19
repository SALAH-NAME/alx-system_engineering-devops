#!/usr/bin/python3
""" 1-export_to_CSV.py """

import csv
import requests
import sys


def export_employee_todo_to_csv(e_id):
    """
    Export_employee_todo_to_csv
    """
    e_url = f'https://jsonplaceholder.typicode.com/users/{e_id}'
    t_url = f'https://jsonplaceholder.typicode.com/users/{e_id}/todos'

    e_resp = requests.get(e_url)
    employee = e_resp.json()

    t_resp = requests.get(t_url)
    todos = t_resp.json()

    data = [
        [
            todo['userId'],
            employee['username'],
            todo['completed'],
            todo['title']
        ]
        for todo in todos
    ]

    with open(f'{e_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == "__main__":
    export_employee_todo_to_csv(sys.argv[1])
