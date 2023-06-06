import random
import prompt
from brain_games import cli
from .brain_games import greeting


def generate_prog():
    massive = []
    s = ''
    first_number = random.randint(1, 20)
    number_of_progression = random.randint(1, 30)
    massive.append(first_number)
    for i in range(9):
        massive.append(massive[i] + number_of_progression)
    answer_numb = random.choice(massive)
    index = random.choice([i for i in range(len(massive)) if massive[i] != answer_numb])
    massive[index] = '..'
    for i in range(len(massive)):
        s += ' ' + str(massive[i])
    return str(answer_numb), s


def prog_game(name: str):
    print('What number is missing in the progression?')
    counter = 0
    while True:
        if counter == 3:
            return f'Congratulations, {name}!'
        response, ask = generate_prog()
        print(f'Question: {ask}')
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


if __name__ == '__main__':
    main()
