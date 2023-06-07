import random
import prompt
from brain_games import cli
from .brain_games import greeting


def generate_prog():
    progression = []
    first_number = random.randint(1, 20)
    number_of_progression = random.randint(1, 30)
    progression.append(first_number)
    for _ in range(9):
        progression.append(progression[-1] + number_of_progression)
    hidden_index = random.randint(0, 9)
    answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(str(num) for num in progression)
    return str(answer), question


def prog_game(name: str):
    print('What number is missing in the progression?')
    counter = 0
    while True:
        if counter == 3:
            return f'Congratulations, {name}!'
        response, question = generate_prog()
        print(f'Question: {question}')
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
    result = prog_game(name)
    print(result)
