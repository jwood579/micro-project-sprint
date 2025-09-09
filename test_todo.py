import subprocess
import sys
import os
import json

todo_script = os.path.join(os.path.dirname(__file__), 'todo.py')
todo_json = os.path.join(os.path.dirname(__file__), 'todo.json')

def run_cmd(args):
    result = subprocess.run([sys.executable, todo_script] + args, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def reset_todo():
    if os.path.exists(todo_json):
        os.remove(todo_json)

def test_invalid_date():
    reset_todo()
    out, err, code = run_cmd(['add', 'Test invalid date', '--due', 'not-a-date'])
    assert code == 0
    assert 'Added: Test invalid date' in out
    with open(todo_json) as f:
        data = json.load(f)
        assert data[0]['due'] == 'not-a-date'
    print('test_invalid_date passed')

def test_remove_out_of_range():
    reset_todo()
    run_cmd(['add', 'Task 1'])
    out, err, code = run_cmd(['remove', '99'])
    assert 'Invalid task number.' in out
    print('test_remove_out_of_range passed')

def test_past_due_red():
    reset_todo()
    run_cmd(['add', 'Past due task', '--due', '2020-01-01'])
    out, err, code = run_cmd(['list'])
    print('DEBUG OUTPUT:', repr(out))
    # Check for ANSI red code and task name
    color_found = any(code in out for code in ['\033[91m', '\x1b[91m', '\u001b[91m', '\u001B[91m'])
    task_found = 'Past due task' in out
    assert color_found and task_found, f"Expected color code and task name in output, got: {repr(out)}"
    print('test_past_due_red passed')

if __name__ == '__main__':
    test_invalid_date()
    test_remove_out_of_range()
    test_past_due_red()
    print('All edge-case tests passed.')
