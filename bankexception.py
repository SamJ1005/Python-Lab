class InsufficientFundsError(Exception):
    pass

balance = 1000   # Initial balance

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == '1':
            print("Current Balance:", balance)

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Amount Deposited Successfully")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                raise InsufficientFundsError("Insufficient Funds!")
            balance -= amount
            print("Withdrawal Successful")

        elif choice == '4':
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input! Please enter numeric value.")

    except InsufficientFundsError as e:
        print(e)