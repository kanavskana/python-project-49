import random


MIN = 1
MAX = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    if random_number < 2:
        return False
    for i in range(2, int(random_number / 2 + 1)):
        if random_number % i == 0:
            return False
    return True


def get_values():
    random_number = random.randint(MIN, MAX)
    question = random_number
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
