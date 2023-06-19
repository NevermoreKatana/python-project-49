import random

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_even(number: int) -> bool:
    return number % 2 == 0


def create_expression():
    number_for_game = random.randint(MIN_NUMBER, MAX_NUMBER)
    response = is_even(number_for_game)
    question = f'Question: {number_for_game}'
    return str(response), question
