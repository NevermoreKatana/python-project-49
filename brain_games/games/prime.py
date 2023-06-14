import random

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def generate_question():
    NUMBER_FOR_GAME = random.randint(1, 50)
    response = is_prime(NUMBER_FOR_GAME)
    question = f'Question: {NUMBER_FOR_GAME}'
    return response, question
