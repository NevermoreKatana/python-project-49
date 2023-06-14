import random

TITLE = 'What is the result of the expression?'


def answer(number, number1, operation):
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    else:
        return number * number1


def generate_question():
    FIRST_NUMBER_FOR_GAME = random.randint(1, 50)
    SECOND_NUMBER_FOR_GAME = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    question = f'Question: {FIRST_NUMBER_FOR_GAME}\
 {operation} {SECOND_NUMBER_FOR_GAME}'
    response = answer(FIRST_NUMBER_FOR_GAME,
                      SECOND_NUMBER_FOR_GAME, operation)
    return response, question
