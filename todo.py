import argparse
import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = '✔' if t['done'] else '✗'
        print(f"{i}. [{status}] {t['task']}")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed: {removed['task']}")
    else:
        print("Invalid task number.")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['task']}")
    else:
        print("Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description='Simple CLI To-Do List')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='Task description')

    list_parser = subparsers.add_parser('list', help='List all tasks')

    remove_parser = subparsers.add_parser('remove', help='Remove a task')
    remove_parser.add_argument('number', type=int, help='Task number to remove (1-based)')

    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('number', type=int, help='Task number to mark as done (1-based)')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'remove':
        remove_task(args.number - 1)
    elif args.command == 'done':
        mark_done(args.number - 1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
