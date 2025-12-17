queue = []

while True:
    print("\n --- Queue ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to enqueue: "))
        queue.append(item)
        print(item, "added to queue")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Removed element:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
