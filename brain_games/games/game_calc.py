import random
import operator


MIN = 1
MAX = 100
DESCRIPTION = 'What is the result of the expression?'


def brain():
    first_num = random.randint(MIN, MAX)
    second_num = random.randint(MIN, MAX)
    operators = {
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub
    }
    selected_oper = random.choice(list(operators))
    question = f'{first_num} {selected_oper} {second_num}'
    correct_answer = str(operators.get(selected_oper)(first_num, second_num))
    return question, correct_answer
