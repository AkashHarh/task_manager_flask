from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
TASKS_FILE = 'tasks.txt'

def read_tasks():
    """Read tasks from the file and return them as a list of tuples (status, description)."""
    try:
        with open(TASKS_FILE, 'r') as file:
            lines = file.readlines()
        tasks = [tuple(line.strip().split(' ', 1)) for line in lines]
    except FileNotFoundError:
        tasks = []
    return tasks

def write_tasks(tasks):
    """Write tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for status, description in tasks:
            file.write(f'{status} {description}\n')

@app.route('/')
def index():
    """Render the main page with the list of tasks."""
    tasks = read_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task to the list."""
    task_description = request.form.get('task')
    if task_description:
        tasks = read_tasks()
        tasks.append(('PENDING', task_description))
        write_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed."""
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        status, description = tasks[task_id]
        if status == 'PENDING':
            tasks[task_id] = ('COMPLETED', description)
            write_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task by its number."""
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        write_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/view')
def view_tasks():
    """View all pending tasks."""
    tasks = read_tasks()
    return render_template('view_tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
