import random
import prompt
import sympy
from brain_games import cli
from brain_games.cli import welcome_user, greet


def prime_game(name: str):
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number = random.randint(1, 50)
        if sympy.isprime(number):
            response = 'yes'
        else:
            response = 'no'
        print(f'Question: {number}')
        answer = prompt.string("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break


def main():
    greet()
    name = welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
