import math
import random
from brain_games import cli
from .brain_games import greeting


def nod_game(name: str):
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        number = random.randint(1, 50)
        nummber1 = random.randint(1, 50)
        response = str(math.gcd(number, nummber1))
        print(f'Question: {number} {nummber1}')
        answer = input("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer \
;(. Correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def main():
    greeting()
    name = cli.welcome_user()
    nod_game(name)
