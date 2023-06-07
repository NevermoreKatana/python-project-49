import random
import prompt
from brain_games import cli
from .brain_games import greeting


def isprime(number: int):
    k = 0
    for i in range(2, number // 2+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False


def prime_game(name: str):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number_ask = random.randint(1, 50)
        if isprime(number_ask) is True:
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
