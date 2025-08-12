# Simple To-Do List Program in Python (No Exception Handling)

todo_list = []  # Store tasks here

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks in the list!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter new task: ")
    todo_list.append(task)
    print("✅ Task added!")

def remove_task():
    view_tasks()
    if todo_list:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"❌ Removed task: {removed}")
        else:
            print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please try again.")
