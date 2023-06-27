import random

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime(number: int):
    k = 0
    if number < 2:
        return True
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    return False


def create_expression():
    number_for_game = random.randint(MIN_NUMBER, MAX_NUMBER)
    response = is_prime(number_for_game)
    response = 'yes' if response else 'no'
    question = f'Question: {number_for_game}'
    return response, question
