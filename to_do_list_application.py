todo_list = []

def add_task(task_name):
    task = {
        'task_name': task_name,
        'is_completed': False
    }
    todo_list.append(task)
    print(f"Task '{task_name}' added to the to-do list.")

def complete_task(task_name):
    task_found = False
    for index, task in enumerate(todo_list):
        if task['task_name'] == task_name:
            task_found = True
            task['is_completed'] = True
            todo_list[index] = task
            print(f"Task '{task_name}' marked as complete.")
    if not task_found:
        print(f"Task '{task_name}' not found.")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for task in todo_list:
            print(f"- {task['task_name']} ({'Completed' if task['is_completed'] else 'Not Completed'})")

def main_menu():
    print("""
    To-Do List Application
    -------------------
    1. Add Task
    2. Complete Task
    3. View Tasks
    4. Quit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == 2:
        task_name = input("Enter task name: ")
        complete_task(task_name)
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        quit()
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    while True:
        main_menu()
