import time
import random
from src.display import rule_book, menu, active_bomb, defused_bomb, bomb_blast,goodbye
from src.user_input import get_player_choice, enter_code
from src.utils import clear_screen
from src.puzzle import sum_puzzle, digit_pattern, reversed_number, mul_puzzle, word_to_number, binary
from src.timer import show_timer

def start_game():
    correct_wire = random.choice(["RED", "BLUE"])
    saved_code = None
    time_remaining = 300
    game_over = False

    while not game_over:

        if time_remaining <= 0:
            bomb_blast()
            game_over = True 
            break

        clear_screen()
        menu()
        active_bomb()
        show_timer(time_remaining)
        choice=get_player_choice()

        if choice == 1:
            if correct_wire == "RED":
                defused_bomb()
            else:
                bomb_blast()
            game_over = True
        
        if choice == 2:
            if correct_wire == "BLUE":
                defused_bomb()
            game_over = True
        
        if choice == 3:
            clear_screen()
            active_bomb()
            if saved_code is None:
                clue_text, saved_code = random_puzzle()
            else:
                clue_text = get_same_clue_again()
            show_hint(clue_text)
            time_remaining -= inspect_time_cost

            wait_for_input_to_continue()

        if choice == 4:
            if saved_code is None:
                 print("You haven't inspected the bomb yet.")
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

