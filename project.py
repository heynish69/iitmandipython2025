# To-Do List Application

def main_menu():
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_task(to_do_list):
    task = input("Enter the task: ")
    to_do_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")
    return to_do_list

def view_tasks(to_do_list):
    if not to_do_list:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

def mark_task_completed(to_do_list):
    view_tasks(to_do_list)
    if not to_do_list:
        return to_do_list
    task_number = int(input("\nEnter the task number to mark as completed: "))
    if 1 <= task_number <= len(to_do_list):
        to_do_list[task_number - 1]["completed"] = True
        print(f"Task '{to_do_list[task_number - 1]['task']}' marked as completed!")
    else:
        print("Invalid task number.")
    return to_do_list

def delete_task(to_do_list):
    view_tasks(to_do_list)
    if not to_do_list:
        return to_do_list
    task_number = int(input("\nEnter the task number to delete: "))
    if 1 <= task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted successfully!")
    else:
        print("Invalid task number.")
    return to_do_list

# Main Program
to_do_list = []
while True:
    choice = main_menu()
    if choice == '1':
        to_do_list = add_task(to_do_list)
    elif choice == '2':
        view_tasks(to_do_list)
    elif choice == '3':
        to_do_list = mark_task_completed(to_do_list)
    elif choice == '4':
        to_do_list = delete_task(to_do_list)
    elif choice == '5':
        print("Thank you for using the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
