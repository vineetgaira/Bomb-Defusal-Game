def main_menu_choice():
    valid_choices={1,2,3,4,5}
    while True:
        choice=int(input("Enter your choie: "))
        try:
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. TRY AGAIN!")
        except valid_choices:
            print("Please enter a valid choice from the menu.")