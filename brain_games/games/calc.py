import random

TITLE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def answer(number, number1, operation):
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    else:
        return number * number1


def generate_question():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    question = f'Question: {first_number}\
 {operation} {second_number}'
    response = answer(first_number,
                      second_number, operation)
    return response, question
