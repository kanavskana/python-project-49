import random


MIN = 1
MAX = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    for i in range(2, int(random_number / 2 + 1)):
        if random_number % i == 0:
            return 'no'
    return 'yes'

def brain():
    random_number = random.randint(MIN, MAX)
    question = random_number
    correct_answer = str(is_prime(random_number))
    return question, correct_answer