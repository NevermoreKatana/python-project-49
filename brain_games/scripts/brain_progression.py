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
    for i in range(10):
        massive.append(massive[i] + number_of_progression)
    answer_numb = random.choice(massive)
    index = massive.index(answer_numb)
    massive.pop(index)
    massive.insert(index, '..')
    for i in range(len(massive)):
        s += ' ' + str(massive[i])
    return str(answer_numb), s


def prog_game(name: str):
    print('What number is missing in the progression?')
    counter = 0
    while True:
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        response, ask = generate_prog()
        print(f'Question: {ask}')
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
    prog_game(name)


if __name__ == '__main__':
    main()
