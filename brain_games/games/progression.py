import random
import prompt


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
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        response, question = generate_prog()
        print(f'Question: {question}')
        answer = prompt.string("Your answer: ")
        if answer == response:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer \
;(. Correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    return f'Congratulations, {name}!'