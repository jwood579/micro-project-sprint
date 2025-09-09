# micro-project-sprint
CLI To-Do list saved to JSON

## Installation & Setup

1. Clone the repository
2. Make sure you have Node.js installed
3. Navigate to the project directory
4. Run `chmod +x todo.js` to make the script executable

## Usage

### Commands

- `node todo.js add <text>` - Add a new todo
- `node todo.js list` - List all todos  
- `node todo.js complete <id>` - Mark a todo as complete
- `node todo.js remove <id>` - Remove a todo
- `node todo.js help` - Show help message

### Examples

```bash
# Add some todos
node todo.js add "Buy groceries"
node todo.js add "Walk the dog"
node todo.js add "Finish project"

# List all todos
node todo.js list

# Mark todo as complete
node todo.js complete 2

# Remove a todo
node todo.js remove 1

# Show help
node todo.js help
```

## Features

- ✅ Add new todos with unique IDs
- ✅ List all todos with completion status
- ✅ Mark todos as complete
- ✅ Remove todos
- ✅ Persistent storage in JSON format
- ✅ Error handling for invalid commands/IDs
- ✅ CLI help system

## Data Storage

Todos are automatically saved to `todos.json` in the current working directory. Each todo includes:
- Unique ID
- Text description
- Completion status
- Creation timestamp
