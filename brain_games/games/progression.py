import random


TITLE = 'What number is missing in the progression?'


def generate_prog():
    progression = []
    first_number = random.randint(1, 20)
    number_of_progression = random.randint(1, 30)
    progression.append(first_number)
    for _ in range(9):
        progression.append(progression[-1] + number_of_progression)
    hidden_index = random.randint(0, 9)
    answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(str(num) for num in progression)
    return str(answer), question


def generate_question():
    response, quest = generate_prog()
    question = f'Question: {quest}'
    return response, question
