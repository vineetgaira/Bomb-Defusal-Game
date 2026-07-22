import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')


def wait_for_input_to_continue():

    move = input()

    return move

