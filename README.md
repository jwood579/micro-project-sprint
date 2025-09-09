# micro-project-sprint

## CLI To-Do List App

This is a simple command-line To-Do list application written in Python. Tasks are saved to a local JSON file for persistence.

### Features
- Add tasks with optional due dates
- List tasks (past due tasks shown in red)
- Mark tasks as done
- Remove tasks
- All data saved in `todo.json`

### Usage
Add a task:
```
python todo.py add "Buy groceries" --due 2025-09-10
```
List tasks:
```
python todo.py list
```
Mark a task as done:
```
python todo.py done 1
```
Remove a task:
```
python todo.py remove 1
```

### Automated Tests
Run edge-case tests:
```
python test_todo.py
```
