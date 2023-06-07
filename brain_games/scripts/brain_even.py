import random
from brain_games import cli
from .brain_games import greeting


def check_number(number: int):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def parity_check_game(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(1, 50)
        response = check_number(number)
        print(f'Question: {number}')
        answer = input("Your answer: ").lower()
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer\
;(. The correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def main():
    greeting()
    name = cli.welcome_user()
    parity_check_game(name)
