import random
from src.display import rule_book, menu, active_bomb, defused_bomb, bomb_blast,goodbye
from src.user_input import get_player_choice
from src.utils import clear_screen

def start_game():

    while True:
        menu()
        active_bomb()
        choice=get_player_choice()
        clear_screen()
        input("Press enter to continue")
        if choice==1 and choice==2:
            random.choice(defused_bomb(),bomb_blast())
            clear_screen()
            input()
        elif choice==5:
            rule_book()
        elif choice==6:
            goodbye()
            return
        else:
            print("Coming soon...")
            

