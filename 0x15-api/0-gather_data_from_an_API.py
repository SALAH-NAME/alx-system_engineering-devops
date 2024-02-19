#!/usr/bin/python3
""" 0-gather_data_from_an_API.py """

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ get_employee_todo_progress """
    employee_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    employee = employee_response.json()

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    )
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    done_task_titles = [todo['title'] for todo in todos if todo['completed']]

    en = employee["name"]
    print(f'Employee {en} is done with tasks({done_tasks}/{total_tasks}):')
    for title in done_task_titles:
        print('\t', title)


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
