import time
import random
from src.display import rule_book, menu, active_bomb, defused_bomb, bomb_blast,goodbye
from src.user_input import get_player_choice
from src.utils import clear_screen
from src.puzzle import sum_puzzle, digit_pattern, reversed_number, mul_puzzle, word_to_number, binary

def start_game():

    while True:
        menu()
        time.sleep(5)
        clear_screen()
        active_bomb()
        choice=get_player_choice()
        clear_screen()
        if choice==1 or choice==2:
            choose_action=random.choice([defused_bomb,bomb_blast])
            choose_action()
            time.sleep(5)
            clear_screen()
        elif choice==5:
            rule_book()
        elif choice==6:
            goodbye()
            return
        else:
            print("Coming soon...")
            
