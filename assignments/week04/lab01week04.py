person = ("Ratchaphol", 25, "Bangkok", "Thailand")
hobbies = ["reading", "eating", "sleeping", "drawing"]

def display_info(person, hobbies):
    print("\n=== Personal Info ===")
    print(f"Name: {person[0]}")
    print(f"Age: {person[1]}")
    print(f"City: {person[2]}")
    print(f"Country: {person[3]}")
    print(f"Hobbies: {', '.join(hobbies)}")

def add_hobby(hobbies):
    new_hobby = input("Enter a new hobby to add: ")
    hobbies.append(new_hobby)
    print(f"Hobby '{new_hobby}' added.")

def remove_hobby(hobbies):
    hobby_to_remove = input("Enter a hobby to remove: ")
    if hobby_to_remove in hobbies:
        hobbies.remove(hobby_to_remove)
        print(f"Hobby '{hobby_to_remove}' removed.")
    else:
        print("Hobby not found.")

def update_age(person):
    new_age = int(input("Enter new age: "))
    person_list = list(person)
    person_list[1] = new_age
    person = tuple(person_list)
    print("Age updated")
    return person

while True:
    print("\n--- MENU ---")
    print("1. Display all info")
    print("2. Add new hobby")
    print("3. Remove hobby")
    print("4. Update age")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        display_info(person, hobbies)
    elif choice == "2":
        add_hobby(hobbies)
    elif choice == "3":
        remove_hobby(hobbies)
    elif choice == "4":
        person = update_age(person)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")