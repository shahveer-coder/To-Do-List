tasks = []

while True:

    print("\n" + "=" * 50)
    print("               TO-DO LIST")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("=" * 50)

    choice = int(input("Enter your choice: "))

    if choice == 1:

        task = input("Enter Task: ")
        tasks.append(task)

        print("\n" + "-" * 50)
        print("Task Added Successfully!")
        print("-" * 50)

    elif choice == 2:

        if len(tasks) == 0:

            print("\n" + "-" * 50)
            print("No Tasks Available")
            print("-" * 50)

        else:

            print("\n" + "-" * 50)
            print("Your Tasks")
            print("-" * 50)

            count = 1

            for task in tasks:
                print(f"{count}. {task}")
                count += 1

            print("-" * 50)

    elif choice == 3:

        if len(tasks) == 0:

            print("\n" + "-" * 50)
            print("No Tasks Available")
            print("-" * 50)

        else:

            print("\nCurrent Tasks")

            count = 1

            for task in tasks:
                print(f"{count}. {task}")
                count += 1

            del_task = int(input("\nEnter Task Number to Delete: "))

            if 1 <= del_task <= len(tasks):

                del tasks[del_task - 1]

                print("\n" + "-" * 50)
                print("Task Deleted Successfully!")
                print("-" * 50)

            else:

                print("\n" + "-" * 50)
                print("Invalid Task Number!")
                print("-" * 50)

    elif choice == 4:

        print("\n" + "=" * 50)
        print("Thank You For Using To-Do List")
        print("=" * 50)
        break

    else:

        print("\n" + "-" * 50)
        print("Invalid Choice!")
        print("Please Enter A Number Between 1 and 4.")
        print("-" * 50)
