import random


def correct_answer(response):
    if response is True:
        return 'yes'
    return 'no'


def play_game(name, game_title, is_correct):
    print(game_title)
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        number = random.randint(1, 50)
        response = is_correct(number)
        print(f'Question: {number}')
        answer = input("Your answer: ").lower()
        if (answer == 'yes' and response) or (answer == 'no' and not response):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer.\
The correct answer was '{correct_answer(response)}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')


def play_game_two_numbers(name, game_title, is_correct, quest):
    print(game_title)
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while counter < NUMBER_OF_ROUNDS:
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        question = quest()
        response = is_correct(first_number, second_number, question)
        print(f'Question: {first_number} {question} {second_number}')
        answer = input("Your answer: ").lower()
        if str(response) == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer.\
The correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
