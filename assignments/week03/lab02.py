balance = 1000.0
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            print("Your balance now = $", balance)
        
        elif choice == "2":
            try:
                withdraw = float(input("Withdraw amount: "))
                if withdraw <= 0:
                    print("Amount must be greater than 0.")
                elif withdraw > balance:
                    print("Insufficient balance.")
                else:
                    balance -= withdraw
                    print("Withdrawal successful. Your balance now = $", balance)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "3":
            try:
                deposit = float(input("Deposit amount: "))
                if deposit <= 0:
                    print("Amount must be greater than 0.")
                else:
                    balance += deposit
                    print("Deposit successful. Your balance now = $", balance)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "4":
            print("Thank for using our banking.")
            break
        
        else:
            print("Invalid option. Please choose 1-4.")
else:
    print("Invalid PIN")
