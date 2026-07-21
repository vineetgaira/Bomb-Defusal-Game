"""These are all the puzzles that will be shown 
after the plyer enters option 3 'inspect bomb'."""
import random

def sum_puzzle():
    a=random.randint(500, 4999)
    b=random.randint(500, 4999)
    code=a+b
    clue_text=f"What is the sum of {a} and {b}?"
    return clue_text, code

def digit_pattern():

    digits=[random.randit(0,7) for _ in range(4)]

    orig=int("".join(map(str,digits)))

    code=int("".join(str((digits * 3) % 7) for d in digits))

    clue_text=f"Hint: Multiply {orig} by 2nd odd number than divide by 4th odd number.\nWhat 'remains' is the code."

    return clue_text, code

def reversed_number():

    number=random.randint(1000,9999)
    code=str(number)
    clue_text=f"Hint: {number} || What if everything was just reversed in the world?"
    return clue_text, int(code[::-1])

def mul_div():
    pass

def date_time():
    pass

def word_to_number():
    pass

def missing_digit():
    pass

def binary():
    pass

def riddle_puzzle():
    pass

def sequence_puzzle():
    pass