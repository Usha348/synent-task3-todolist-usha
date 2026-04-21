tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number")
            except:
                print("Enter valid number")

    elif choice == '4':
        print("Exiting To-Do List")
        break

    else:
        print("Invalid choice")