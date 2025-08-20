import json
import os

# Define the file where tasks will be saved
TODO_FILE = 'tasks.json'

def load_tasks():
    """Loads tasks from the JSON file. Creates an empty file if it doesn't exist."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        status = "✓" if task['completed'] else " "
        print(f"{i + 1}. [{status}] {task['task']}")
    print("-----------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    task_description = input("Enter the new task: ")
    if task_description:
        tasks.append({'task': task_description, 'completed': False})
        print(f"Task '{task_description}' added.")
    else:
        print("Task description cannot be empty.")
    save_tasks(tasks)

def complete_task(tasks):
    """Marks a task as complete."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to complete: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    save_tasks(tasks)

def delete_task(tasks):
    """Deletes a task from the list."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to delete: "))
        if 0 < task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    save_tasks(tasks)

def show_menu():
    """Displays the main menu options."""
    print("\nCommand-Line To-Do List")
    print("------------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    print("------------------------")

def main():
    """The main function to run the application."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
