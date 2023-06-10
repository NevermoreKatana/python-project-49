import random
from brain_games import cli
from .brain_games import greeting


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def parity_check_game(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        number = random.randint(1, 50)
        response = is_even(number)
        print(f'Question: {number}')
        answer = input("Your answer: ").lower()
        if (answer == 'yes' and response) or (answer == 'no' and not response):
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
