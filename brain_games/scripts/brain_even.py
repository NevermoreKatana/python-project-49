import random
import prompt
from brain_games import cli
from .brain_games import greeting


def parity_check_game(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    max_attempts = 3
    while counter < max_attempts:
        number = random.randint(1, 50)
        if number % 2 == 0:
            response = 'yes'
        else:
            response = 'no'
        print(f'Question: {number}')
        answer = input("Your answer: ").lower()
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer ;(. The correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def main():
    greeting()
    name = cli.welcome_user()
    parity_check_game(name)
