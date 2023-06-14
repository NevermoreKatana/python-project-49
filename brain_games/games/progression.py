import random


TITLE = 'What number is missing in the progression?'


def generate_prog():
    progression = []
    FIRST_NUMBER = random.randint(1, 20)
    NUMBER_OF_PROGRESSION = random.randint(1, 30)
    progression.append(FIRST_NUMBER)
    for _ in range(9):
        progression.append(progression[-1] + NUMBER_OF_PROGRESSION)
    HIDDEN_INDEX = random.randint(0, 9)
    answer = progression[HIDDEN_INDEX]
    progression[HIDDEN_INDEX] = '..'
    question = ' '.join(str(num) for num in progression)
    return str(answer), question


def generate_question():
    response, quest = generate_prog()
    question = f'Question: {quest}'
    return response, question
