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
    code=[]
    for i in range(0,8):
        i+=2
        if len(code)<=4:
            code.append(i)
    return int("".join(map(str, code)))

def reversed_number():
    pass

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