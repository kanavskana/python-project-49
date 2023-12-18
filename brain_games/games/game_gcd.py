import random
from math import gcd


MIN = 1
MAX = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def brain():
    first_number = random.randint(MIN, MAX)
    second_number = random.randint(MIN, MAX)
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer
