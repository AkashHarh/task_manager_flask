# Task Manager Flask Application

This is a Flask application that provides a web-based user interface to manage tasks. The application provides functionality for viewing, adding, completing, and deleting tasks.

## Application Routes and Functions

### 1. Home Page (`/`)
- **Function**: `index()`
- **Description**: Returns the main page with a list of all tasks.

### 2. Add Task (`/add`)
- **Function**: `add_task()`
- **Description**: Adds a new task to the list.

### 3. Complete Task (`/complete/<int:task_id>`)
- **Function**: `complete_task(task_id)`
- **Description**: Marks a given task as completed.

### 4. Delete Task (`/delete/<int:task_id>`)
- **Function**: `delete_task(task_id)`
- **Description**: Deletes a task by ID.

### 5. View Tasks (`/view`)
- **Function**: `view_tasks()`
- **Description**: Lists all tasks, both pending and completed.

## Helper Functions

### 1. Read Tasks
- **Function**: `read_tasks()`
- **Description**: Reads the tasks from the file and returns them as a list of tuples.

### 2. Write Tasks
- **Function**: `write_tasks(tasks)`
- **Description**: Writes the list of tasks to the file.

## Run Application

1. **Install Dependencies**: Ensure Flask is installed.
2. **Start Application**: Run `python app.py` to start the server.

The application can be accessed at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## License

This project is licensed under the MIT License.
