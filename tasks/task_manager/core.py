import json
import os
from logger import setup_logger

TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")
logger = setup_logger()

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "priority": priority})
    save_tasks(tasks)
    logger.info(f"Added task: {description} with priority {priority}")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")
    logger.info("Listed all tasks")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    logger.info(f"Deleted task with ID: {task_id}")