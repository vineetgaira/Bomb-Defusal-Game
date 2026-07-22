import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')




"""
This is will be my main game loop:

START:
    # --- SETUP (runs once, before the loop) ---
    correct_wire = random.choice(["RED", "BLUE"])   # decided once, secretly
    saved_code = None                                # no code exists yet
    time_remaining = 300                             # e.g. 5:00 in seconds
    game_over = False

    WHILE NOT game_over:

        # --- TIMER CHECK FIRST, before player gets another turn ---
        IF time_remaining <= 0:
            show_bomb_blast()
            show_you_lose_banner()
            game_over = True
            BREAK

        clear_screen()
        show_main_menu()
        show_active_bomb_art()
        show_timer(time_remaining)
        choice = get_player_choice()

        IF choice == 1:                # Cut RED wire
            IF correct_wire == "RED":
                show_bomb_defused()
                show_you_win_banner()
            ELSE:
                show_bomb_blast()
                show_you_lose_banner()
            game_over = True

        IF choice == 2:                # Cut BLUE wire
            IF correct_wire == "BLUE":
                show_bomb_defused()
                show_you_win_banner()
            ELSE:
                show_bomb_blast()
                show_you_lose_banner()
            game_over = True

        IF choice == 3:                # Inspect bomb
            clear_screen()
            show_active_bomb_art()
            IF saved_code IS None:
                clue_text, saved_code = random_puzzle()   # generate once
            ELSE:
                clue_text = get_same_clue_again()          # or re-show last clue
            show_hint(clue_text)
            time_remaining -= inspect_time_cost            # optional: inspecting costs time
            wait_for_input_to_continue()

        IF choice == 4:                # Enter code
            IF saved_code IS None:
                show_message("You haven't inspected the bomb yet.")
            ELSE:
                guess = get_code_input()          # string, validated: isdigit() and len == 4
                IF guess == saved_code:
                    show_bomb_defused()
                    show_you_win_banner()
                    game_over = True
                ELSE:
                    show_bomb_blast()
                    show_you_lose_banner()
                    game_over = True

        IF choice == 5:                # Rules
            clear_screen()
            show_rulebook()
            wait_for_input_to_continue()

        IF choice == 6:                # Exit
            show_goodbye_message()
            game_over = True

    END WHILE
END
     
"""