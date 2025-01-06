# To-Do App

This is a simple command-line-based To-Do application written in Python. The app allows users to manage their daily tasks by adding, viewing, and deleting tasks. Tasks are stored in a JSON file, ensuring data persistence between sessions.

## Features

1. **Add Task**: Add a new task to the to-do list.
2. **View Tasks**: View all the tasks in the list.
3. **Delete Task**: Remove a task from the list by specifying its number.
4. **Quit**: Exit the application.

## Requirements

- Python 3.x

## How to Use

### 1. Clone or Download the Repository

Download the code to your local machine.

### 2. Run the Application

Run the script in your terminal or command prompt:

```bash
python todo_app.py
```

### 3. Menu Options

The application provides the following menu options:

- **1. Add Task**: Enter a new task to add it to the list.
- **2. View Tasks**: Displays all saved tasks with their corresponding numbers.
- **3. Delete Task**: Removes a task from the list by its number.
- **4. Quit**: Exit the application.

### 4. Example Interaction

```plaintext
To Do App
1. Add Task
2. View Task
3. Delete Task
4. Quit

Please enter your choice: 1

Enter your task: Buy groceries

Task added: Buy groceries

To Do App
1. Add Task
2. View Task
3. Delete Task
4. Quit

Please enter your choice: 2

1. Buy groceries

To Do App
1. Add Task
2. View Task
3. Delete Task
4. Quit

Please enter your choice: 3

Enter your task number you want to delete: 1

Task deleted: Buy groceries

To Do App
1. Add Task
2. View Task
3. Delete Task
4. Quit

Please enter your choice: 4

Thank you for using my program!
```

## Code Breakdown

### File Operations

- **`load_task()`**: Reads tasks from `tasks.json`. If the file doesn't exist or is invalid, it returns an empty list.
- **`save_task()`**: Writes the current list of tasks to `tasks.json`.

### Main Functions

- **`add_task()`**: Prompts the user to enter a task and saves it to the list.
- **`view_task()`**: Displays all tasks in the list with a numbered format.
- **`del_task()`**: Deletes a task by its number and updates the list.

### User Interaction

- **`show_menu()`**: Displays the main menu.
- A `while` loop ensures continuous operation until the user chooses to quit.

## Error Handling

- Handles `FileNotFoundError` and `JSONDecodeError` during task loading.
- Validates user input for task addition and deletion.

## Data Storage

Tasks are stored in a file named `tasks.json` in the same directory as the script. This ensures data is persistent even after the program exits.

## Notes

- Ensure `tasks.json` is in the same directory as the script or it will be created automatically.
- Enter valid numbers when choosing menu options or deleting tasks.

## Future Improvements

- Add options to mark tasks as completed.
- Include due dates or priority levels for tasks.
- Implement a graphical user interface (GUI).

---

Enjoy managing your tasks with this simple To-Do app! Feel free to modify and extend the code to suit your needs.
