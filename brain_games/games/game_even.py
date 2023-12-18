from random import randint


MIN = 1
MAX = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def brain():
    random_number = randint(MIN, MAX)

    if number(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer

def number(random_number):
        return random_number % 2 == 0