phonebook = {}

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add contact
    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added successfully!")

    # Search contact
    elif choice == 2:
        name = input("Enter name to search: ")
        if name in phonebook:
            print("Phone number:", phonebook[name])
        else:
            print("Contact not found!")

    # Delete contact
    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Exit program
    elif choice == 4:
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice! Try again.")
