import random
import operator


MIN = 1
MAX = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def brain():
    first_number = random.randint(MIN, MAX)
    second_number = random.randint(MIN, MAX)
    operators = {
         '*': operator.mul,
         '+': operator.add,
         '-': operator.sub
    }
    selected_operator = random.choice(list(operators))
    question = f'{first_number} {selected_operator} {second_number}'
    correct_answer = str(operators.get(selected_operator)(first_number,second_number))
    return question, correct_answer