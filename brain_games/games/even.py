import random


TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

def generate_question():
    NUMBER_FOR_GAME = random.randint(1, 50)
    response = is_even(NUMBER_FOR_GAME)
    question = f'Question: {NUMBER_FOR_GAME}'
    return response, question