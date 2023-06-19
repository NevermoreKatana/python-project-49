import random

TITLE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def calculate_result(number, number1, operation):
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    return number * number1


def create_expression():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    question = f'Question: {first_number}\
 {operation} {second_number}'
    response = calculate_result(first_number,
                                second_number, operation)
    return str(response), question
