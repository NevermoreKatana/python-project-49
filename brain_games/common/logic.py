import random


NUMBER_OF_ROUNDS = 3


def correct_answer(response):
    if response is True:
        return 'yes'
    return 'no'


def play_game(name, game_title, func_gen_question):
    print(game_title)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        response, question = func_gen_question()
        print(question)
        answer = input("Your answer: ").lower()
        if (answer == 'yes' and response) or (answer == 'no' and not response):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is the wrong answer ;(.\
 Correct answer was '{correct_answer(response)}'")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


def play_game_two_numbers(name, game_title, is_correct, quest):
    print(game_title)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        question = quest()
        FIRST_NUMBER_FOR_GAME = random.randint(1, 50)
        SECOND_NUMBER_FOR_GAME = random.randint(1, 50)
        response = is_correct(FIRST_NUMBER_FOR_GAME,
                              SECOND_NUMBER_FOR_GAME, question)
        print(f'Question: {FIRST_NUMBER_FOR_GAME}\
 {question} {SECOND_NUMBER_FOR_GAME}')
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
