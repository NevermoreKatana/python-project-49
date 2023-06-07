import random
import prompt
from brain_games import cli
from .brain_games import greeting


def isprime(number: int):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def prime_game(name: str):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0

    while counter < 3:
        number_ask = random.randint(1, 50)
        is_prime = isprime(number_ask)
        print(f'Question: {number_ask}')
        answer = prompt.string("Your answer: ")

        if (answer == 'yes' and is_prime) or (answer == 'no' and not is_prime):
            print('Correct!')
            counter += 1
        else:
            correct_answer = 'yes' if is_prime else 'no'
            print(f"'{answer}' is the wrong answer ;(. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')



def main():
    greeting()
    name = cli.welcome_user()
    prime_game(name)
