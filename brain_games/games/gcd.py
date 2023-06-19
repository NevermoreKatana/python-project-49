import math
import random

TITLE = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def create_expression():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    response = math.gcd(first_number, second_number)
    question = f'Question: {first_number} {second_number}'
    return response, question
