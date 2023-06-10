import random
from brain_games import cli
from .brain_games import greeting


def generate_question():
    number = random.randint(1, 50)
    number1 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    return number, number1, operation


def check_answer(number, number1, operation):
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    else:
        return number * number1


def calc_game(name: str):
    print('What is the result of the expression?')
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        number, number1, operation = generate_question()
        print(f'Question: {number} {operation} {number1}')
        answer = input("Your answer: ")
        correct_answer = check_answer(number, number1, operation)
        if str(correct_answer) == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer. \
The correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def main():
    greeting()
    name = cli.welcome_user()
    calc_game(name)
