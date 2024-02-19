#!/usr/bin/python3
""" 3-dictionary_of_list_of_dictionaries.py """

import json
import requests


def export_all_employee_todo_to_json():
    """ export_all_employee_todo_to_json """
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    data = {}

    for user in users:
        fstr = f'https://jsonplaceholder.typicode.com/users/{user["id"]}/todos'
        todos_response = requests.get(fstr)
        todos = todos_response.json()

        data[user['id']] = [
            {
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_all_employee_todo_to_json()
