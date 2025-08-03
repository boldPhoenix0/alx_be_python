def display_menu():
    """Displays the menu options for the shopping list manager."""
    # Ensure the correct print statement format
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# fns_and_dsa/shopping_list_manager.py

def display_menu():
    """Displays the menu options for the shopping list manager."""
    # Display the menu title
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function that runs the shopping list manager."""
    
    # Ensure that shopping_list is a list
    shopping_list = []
    if not isinstance(shopping_list, list):
        raise TypeError("shopping_list must be a list")

    while True:
        # Check if display_menu function is callable
        if not callable(display_menu):
            raise NameError("display_menu function is not defined or callable")
        
        # Call display_menu function
        display_menu()

        # Ensure choice input is a number (integer)
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Handle the user's choice
        if choice == 1:
            # Prompt the user to add an item using the exact input statement requested
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == 2:
            # Prompt the user to remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            # Display the current shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()