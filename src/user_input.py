import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def get_player_choice():
    valid_choices={1,2,3,4,5,6}
    while True:
        try:
            choice=int(input(Fore.LIGHTBLUE_EX+"Enter your choie: "))
            if choice in valid_choices:
                return choice
            else:
                print(Fore.RED+"Invalid choice. TRY AGAIN!")
        except ValueError:
            print(Fore.RED+"Invalid choice. ENTER A NUMBER!")

def enter_code():
    while True:
        code=input(Fore.LIGHTBLUE_EX+"Enter the code: ")
        if len(code)==4 and code.isdigit():
            return code
        else:
            print(Fore.RED+Style.BRIGHT+"Please enter a valid length or number!"+Style.RESET_ALL)
   