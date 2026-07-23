import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import time
import random
from src.display import rule_book, menu, active_bomb, defused_bomb, bomb_blast,goodbye
from src.user_input import get_player_choice, enter_code
from src.utils import clear_screen, wait_for_input_to_continue
from src.puzzle import random_puzzle, sum_puzzle, digit_pattern, reversed_number, mul_puzzle, word_to_number, binary
# from src.timer import show_timer

def start_game():
    puzzles = [sum_puzzle, digit_pattern, reversed_number, mul_puzzle, word_to_number, binary]
    correct_wire = random.choice(["RED", "BLUE"])
    saved_code = None
    clue_text = None
    chances= 3
    inspection_cost = 1
    game_over = False

    menu()
    wait_for_input_to_continue()
    clear_screen()
    while not game_over:

        if chances<= 0:
            bomb_blast()
            game_over = True 
            break

        active_bomb()
        print(Fore.BLUE+f"Chances : {Fore.RED+str(chances)}")
        choice=get_player_choice()

        if choice == 1:
            clear_screen()
            time.sleep(1)
            if correct_wire == "RED":
                defused_bomb()
            else:
                bomb_blast()
            game_over = True
        
        if choice == 2:
            clear_screen()
            time.sleep(1)
            if correct_wire == "BLUE":
                defused_bomb()
            else:
                bomb_blast()
            game_over = True
            
        
        if choice == 3:
            clear_screen()
            active_bomb()
            if saved_code is None and clue_text is None:
                clue_text, saved_code = random_puzzle(puzzles)
            print(Fore.GREEN+clue_text)

            chances-= inspection_cost

            wait_for_input_to_continue()

        if choice == 4:
            if saved_code is None:
                 print(Fore.RED+Style.BRIGHT+"You haven't inspected the bomb yet."+Style.RESET_ALL)
            else:
                guess = enter_code()

                if guess == saved_code:
                    defused_bomb()
                    game_over = True
                else:
                    bomb_blast()
                    game_over = True

        if choice == 5:
            clear_screen()
            rule_book()
            wait_for_input_to_continue()

        if choice == 6:
            goodbye()
            game_over = True