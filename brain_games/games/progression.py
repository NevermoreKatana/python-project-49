import random

LONG_PROGRESSION = 9
TITLE = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def generate_prog():
    progression = []
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    step_of_progression = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression.append(first_number)
    for _ in range(LONG_PROGRESSION):
        progression.append(progression[-1] + step_of_progression)
    HIDDEN_INDEX = random.randint(0, LONG_PROGRESSION - 1)
    answer = progression[HIDDEN_INDEX]
    progression[HIDDEN_INDEX] = '..'
    question = ' '.join(str(num) for num in progression)
    return str(answer), question


def create_expression():
    response, quest = generate_prog()
    question = f'Question: {quest}'
    return response, question
