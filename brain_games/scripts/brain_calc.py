import random
import prompt
from brain_games import cli
from .brain_games import greeting


def generate_question():
    number = random.randint(1, 50)
    number1 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    return number, number1, operation


def check_answer(number, number1, operation, answer):
    if operation == '+':
        return number + number1 == answer
    elif operation == '-':
        return number - number1 == answer
    else:
        return number * number1 == answer


def calc_game(name: str):
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        number, number1, operation = generate_question()
        print(f'Question: {number} {operation} {number1}')
        answer = int(input("Your answer: "))
        if check_answer(number, number1, operation, answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(str(number) + operation + str(number1))}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def main():
    greeting()
    name = cli.welcome_user()
    calc_game(name)
