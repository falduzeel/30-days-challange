balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("Login Successful")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your Balance:", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
                print("New Balance:", balance)
            else:
                print("Invalid Amount")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid Amount")
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")
