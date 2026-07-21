"""These are all the puzzles that will be shown 
after the plyer enters option 3 'inspect bomb'."""
import random
import math

def sum_puzzle():
    a=random.randint(500, 4999)
    b=random.randint(500, 4999)
    code=a+b
    clue_text=f"What is the sum of {a} and {b}?"
    return clue_text, str(code)

def digit_pattern():

    digits=[random.randint(0,7) for _ in range(4)]

    orig=int("".join(map(str,digits)))

    code="".join(str((d * 3) % 7) for d in digits)

    clue_text=f"Hint: Multiply each digit of {orig} by 2nd odd number than divide by 4th odd number.\nWhat 'remains' is the code."

    return clue_text, code

def reversed_number():

    number=random.randint(1000,9999)
    code=str(number)
    clue_text=f"Hint: {number} || What if everything was just reversed in the world?"
    return clue_text, code[::-1]

def mul_puzzle():

    A = random.randint(1,999)

    min_B=math.ceil(1000/A)
    max_B=math.floor(9999/A)

    B=random.choice([min_B,max_B])

    code=A*B
    clue_text=f"Hint: || {A} X {B} ||"

    return clue_text, str(code) 

def date_time():
    pass

def word_to_number():

    alpha_num_map={
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J"
    }

    digits=[random.randint(0, 9) for _ in range(4)]
    
    letters="".join(alpha_num_map[d] for d in digits) 
    code="".join(str(d) for d in digits)

    clue_text=("If A = 0, B = 1 and C = 3....up to J = 9.\n"
               f"Then the code is: {letters}")

    return clue_text, code

def missing_digit():
    pass

def binary():

    code = random.randint(1000, 9999)

    binary_string = bin(code) [2:]

    clue_text=f"This is another form of code :{binary_string}"

    return clue_text, str(code)

def riddle_puzzle():
    pass

def sequence_puzzle():
    pass