from random import randint


MIN = 1
MAX = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_values():
    random_number = randint(MIN, MAX)

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer


def is_even(random_number):
    return random_number % 2 == 0
