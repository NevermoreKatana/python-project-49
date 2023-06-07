import math
import random
import prompt
from brain_games import cli
from .brain_games import greeting


def nod_game(name: str):
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number, nummber1 = random.randint(1, 50), random.randint(1, 50)
        response = str(math.gcd(number, nummber1))
        print(f'Question: {number} {nummber1}')
        answer = prompt.string("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was \
'{response}'\nLet's try again, {name}!"


def main():
    greeting()
    name = cli.welcome_user()
    nod_game(name)


if __name__ == '__main__':
    main()
