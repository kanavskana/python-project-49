import random


DESCRIPTION = 'What number is missing in the progression?'


def get_values():
    progression_start = random.randint(1, 20)
    length = random.randint(5, 10)
    progression = list(progression_start * i for i in range(1, length + 1))
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(prog) for prog in progression)
    return question, correct_answer
