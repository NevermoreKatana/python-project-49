import random
import prompt
from brain_games import cli
from .brain_games import greeting


def parity_check_game(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number = random.randint(1, 50)
        if number % 2 == 0:
            response = 'yes'
        else:
            response = 'no'
        print(f'Question: {number}')
        answer = prompt.string("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was \
'{response}'\nLet's try again, {name}!")


def main():
    greeting()
    name = cli.welcome_user()
    parity_check_game(name)
