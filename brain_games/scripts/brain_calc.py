import random
import prompt
from brain_games import cli
from .brain_games import greeting


def calc_game(name: str):
    print('What is the result of the expression?')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        number = random.randint(1, 50)
        number1 = random.randint(1, 50)
        operation = random.choice('*+-')
        if operation == '+':
            response = str(number + number1)
        elif operation == '-':
            response = str(number - number1)
        else:
            response = str(number * number1)
        print(f'Question: {number} {operation} {number1}')
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
    calc_game(name)


if __name__ == '__main__':
    main()
