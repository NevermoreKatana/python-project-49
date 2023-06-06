import random
import prompt
import sympy
from brain_games import cli
from .brain_games import greeting


def prime_game(name: str):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number_ask = random.randint(1, 50)
        if sympy.isprime(number_ask) is True:
            response = 'yes'
        else:
            response = 'no'
        print(f'Question: {number_ask}')
        answer = prompt.string("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
'{response}'\nLet's try again, {name}!")
            break


def main():
    greeting()
    name = cli.welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
