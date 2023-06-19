import random

LONG_PROGRESSION = 9
TITLE = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def generate_prog(f_num, step, long):
    progression = []
    progression.append(f_num)
    for _ in range(long):
        progression.append(progression[-1] + step)
    return progression


def create_expression():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    step_of_progression = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = generate_prog(first_number, step_of_progression,
                                LONG_PROGRESSION)
    hidden_index = random.randint(0, LONG_PROGRESSION - 1)
    response = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(str(num) for num in progression)}"
    return response, question
