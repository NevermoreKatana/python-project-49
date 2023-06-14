import math
import random

TITLE = 'Find the greatest common divisor of given numbers.'


def generate_question():
    FIRST_NUMBER_FOR_GAME = random.randint(1, 50)
    SECOND_NUMBER_FOR_GAME = random.randint(1, 50)
    response = math.gcd(FIRST_NUMBER_FOR_GAME, SECOND_NUMBER_FOR_GAME)
    question = f'Question: {FIRST_NUMBER_FOR_GAME} {SECOND_NUMBER_FOR_GAME}'
    return response, question
