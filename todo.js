#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const TODO_FILE = path.join(process.cwd(), 'todos.json');

// Load todos from JSON file
function loadTodos() {
  try {
    if (fs.existsSync(TODO_FILE)) {
      const data = fs.readFileSync(TODO_FILE, 'utf8');
      return JSON.parse(data);
    }
  } catch (error) {
    console.error('Error loading todos:', error.message);
  }
  return [];
}

// Save todos to JSON file
function saveTodos(todos) {
  try {
    fs.writeFileSync(TODO_FILE, JSON.stringify(todos, null, 2));
  } catch (error) {
    console.error('Error saving todos:', error.message);
  }
}

// Generate unique ID for new todos
function generateId(todos) {
  return todos.length > 0 ? Math.max(...todos.map(t => t.id)) + 1 : 1;
}

// Add a new todo
function addTodo(text) {
  const todos = loadTodos();
  const newTodo = {
    id: generateId(todos),
    text: text,
    completed: false,
    createdAt: new Date().toISOString()
  };
  todos.push(newTodo);
  saveTodos(todos);
  console.log(`Added todo: "${text}" (ID: ${newTodo.id})`);
}

// List all todos
function listTodos() {
  const todos = loadTodos();
  if (todos.length === 0) {
    console.log('No todos found.');
    return;
  }
  
  console.log('\nTodo List:');
  console.log('----------');
  todos.forEach(todo => {
    const status = todo.completed ? '✓' : '○';
    console.log(`${status} [${todo.id}] ${todo.text}`);
  });
  console.log('');
}

// Mark todo as complete
function completeTodo(id) {
  const todos = loadTodos();
  const todo = todos.find(t => t.id === parseInt(id));
  
  if (!todo) {
    console.log(`Todo with ID ${id} not found.`);
    return;
  }
  
  todo.completed = true;
  saveTodos(todos);
  console.log(`Marked todo "${todo.text}" as complete.`);
}

// Remove a todo
function removeTodo(id) {
  const todos = loadTodos();
  const index = todos.findIndex(t => t.id === parseInt(id));
  
  if (index === -1) {
    console.log(`Todo with ID ${id} not found.`);
    return;
  }
  
  const removedTodo = todos.splice(index, 1)[0];
  saveTodos(todos);
  console.log(`Removed todo: "${removedTodo.text}"`);
}

// Show usage help
function showHelp() {
  console.log(`
Todo CLI - A simple command-line todo list

Usage:
  todo add <text>       Add a new todo
  todo list             List all todos
  todo complete <id>    Mark todo as complete
  todo remove <id>      Remove a todo
  todo help             Show this help message

Examples:
  todo add "Buy groceries"
  todo list
  todo complete 1
  todo remove 2
`);
}

// Main CLI logic
function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  switch (command) {
    case 'add':
      if (args.length < 2) {
        console.log('Error: Please provide todo text.');
        console.log('Usage: todo add <text>');
        process.exit(1);
      }
      addTodo(args.slice(1).join(' '));
      break;

    case 'list':
      listTodos();
      break;

    case 'complete':
      if (args.length < 2) {
        console.log('Error: Please provide todo ID.');
        console.log('Usage: todo complete <id>');
        process.exit(1);
      }
      completeTodo(args[1]);
      break;

    case 'remove':
      if (args.length < 2) {
        console.log('Error: Please provide todo ID.');
        console.log('Usage: todo remove <id>');
        process.exit(1);
      }
      removeTodo(args[1]);
      break;

    case 'help':
    case '--help':
    case '-h':
      showHelp();
      break;

    default:
      if (!command) {
        showHelp();
      } else {
        console.log(`Unknown command: ${command}`);
        showHelp();
        process.exit(1);
      }
  }
}

// Run the CLI
if (require.main === module) {
  main();
}

module.exports = { loadTodos, saveTodos, addTodo, listTodos, completeTodo, removeTodo };