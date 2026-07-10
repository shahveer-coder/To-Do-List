tasks = []
while True:
    print("=" * 45)
    print("          TO-DO LIST")
    print("=" * 45)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user = input("Enter Task: ")
        tasks.append(user)
        print("Task Added Successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("\nNo Tasks Available")
        else:
            count = 1
            print("Your Tasks")
            for task in tasks:
                print(count,task)
                count += 1
            
    elif choice == 3:
        del_task = input(input("Enter Task to Delete: "))
        if del_task == count:
            
            print("Task Deleted Successfully!")