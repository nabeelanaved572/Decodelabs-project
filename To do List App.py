# Creating an empty list 
todo_list = []

# Function to add a new task  
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New Task Added Successfully!")

# Function to view all tasks
def view_task():
    print("\nYour Todo List:")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")

# Function to remove a task
def remove_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter the number of the task you want to delete: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid Task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Function to mark a task as done
def mark_done():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1 
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task '{todo_list[search_index]['Task']}' has been marked as Done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Function to display a menu
def menu():
    while True:
        print("\nMain Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice!")

# Start the program
if __name__ == "__main__":
    menu()
