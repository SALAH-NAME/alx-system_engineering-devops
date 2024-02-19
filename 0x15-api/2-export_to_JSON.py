#!/usr/bin/python3
""" 2-export_to_JSON.py """

import json
import requests
import sys


def export_employee_todo_to_json(e_id):
    """
    export_employee_todo_to_json
    """
    employee_url = f'https://jsonplaceholder.typicode.com/users/{e_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{e_id}/todos'

    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    data = {
        e_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee['username']
            }
            for todo in todos
        ]
    }

    with open(f'{e_id}.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_employee_todo_to_json(sys.argv[1])
