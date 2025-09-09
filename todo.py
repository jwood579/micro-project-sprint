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

def add_task(task, due=None):
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False, 'due': due})
    save_tasks(tasks)
    if due:
        print(f"Added: {task} (Due: {due})")
    else:
        print(f"Added: {task}")

def list_tasks():
    tasks = load_tasks()
    output = []
    if not tasks:
        output.append("No tasks found.")
    else:
        from datetime import datetime
        for i, t in enumerate(tasks, 1):
            status = 'X' if t['done'] else ' '
            due = t.get('due')
            due_str = f" (Due: {due})" if due else ''
            is_past_due = False
            if due and not t['done']:
                try:
                    due_date = datetime.strptime(due, "%Y-%m-%d")
                    if due_date.date() < datetime.now().date():
                        is_past_due = True
                except Exception:
                    pass
            color_start = '\033[91m' if is_past_due else ''
            color_end = '\033[0m' if is_past_due else ''
            output.append(f"{color_start}{i}. [{status}] {t['task']}{due_str}{color_end}")
    return '\n'.join(output)

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
    # ...existing code...
    parser = argparse.ArgumentParser(description='Simple CLI To-Do List')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='Task description')
    add_parser.add_argument('--due', type=str, help='Due date (e.g. 2025-09-10)', default=None)

    list_parser = subparsers.add_parser('list', help='List all tasks')

    remove_parser = subparsers.add_parser('remove', help='Remove a task')
    remove_parser.add_argument('number', type=int, help='Task number to remove (1-based)')

    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('number', type=int, help='Task number to mark as done (1-based)')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task, args.due)
    elif args.command == 'list':
        print(list_tasks(), flush=True)
    elif args.command == 'remove':
        remove_task(args.number - 1)
    elif args.command == 'done':
        mark_done(args.number - 1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
