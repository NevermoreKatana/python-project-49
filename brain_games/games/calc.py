import random

TITLE = 'What is the result of the expression?'


def generate_question():
    operation = random.choice(['+', '-', '*'])
    return operation


def check_answer(number, number1, operation):
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    else:
        return number * number1
