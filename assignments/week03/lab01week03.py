# Complete this program to classify people by age


# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
while True:
    user_input = input("Enter age (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Thank for use our program")
        break 

    try:
        age = int(user_input)
        
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        elif age <= 12:
            print("You're a Child.")
        elif age <= 19:
            print("You're a Teenager.")
        elif age <= 59:
            print("You're an Adult.")
        else:
            print("You're a Senior.")
    
    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.")
