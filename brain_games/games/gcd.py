import math
import random


def nod_game(name: str):
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        number = random.randint(1, 50)
        nummber1 = random.randint(1, 50)
        response = str(math.gcd(number, nummber1))
        print(f'Question: {number} {nummber1}')
        answer = input("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer \
;(. Correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')