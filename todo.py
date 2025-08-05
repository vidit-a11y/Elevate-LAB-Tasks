TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

print("\n WELCOME TO YOUR TO-DO LIST ")

while True:
    print("\nPlease select an option:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")             
    print("4. Mark a task as complete")  
    print("5. Exit")                     

    choice = input("Enter your choice (1-5): ") 

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        save_tasks(tasks) 
        print(f"Task '{task}' added successfully")

    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty")
        else:
            print("\n Your Tasks ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
 
    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty, nothing to update")
        else:
            print("\nSelect a task number to update:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            
            try:
                task_number = int(input("Enter the task number: "))
                if 1 <= task_number <= len(tasks):
                    new_task_text = input("Enter the new task text: ")
                    
                    tasks[task_number - 1] = new_task_text
                    save_tasks(tasks) 
                    print(f"Task {task_number} has been updated successfully")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input, Please enter a number")

    elif choice == '4': 
        if not tasks:
            print("Your to-do list is empty, nothing to remove.")
        else:
            print("\nSelect a task number to mark as complete:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            
            try:
                task_to_remove = int(input("Enter the task number: "))
                if 1 <= task_to_remove <= len(tasks):
                    removed_task = tasks.pop(task_to_remove - 1)
                    save_tasks(tasks) 
                    print(f"Task '{removed_task}' completed and removed")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Invalid input, Please enter a number")

    elif choice == '5': 
        print("Thank you for using the to-do list")
        break

    else:
        print("Invalid choice, Please enter a number between 1 and 5") 