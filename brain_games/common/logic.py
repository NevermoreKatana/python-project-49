NUMBER_OF_ROUNDS = 3


def play_game(name, game_title, func_gen_question):
    print(game_title)
    for counter in range(NUMBER_OF_ROUNDS):
        response, question = func_gen_question()
        print(question)
        answer = input("Your answer: ").lower()
        if (answer == 'yes' and response) or (answer == 'no' and not response)\
                or (answer == response):
            print('Correct!')
        else:
            print(f"'{answer}' is the wrong answer ;(. "
                  f"Correct answer was '{'yes' if response else 'no'}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
