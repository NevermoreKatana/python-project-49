NUMBER_OF_ROUNDS = 3


def play_game(name, game_title, func_gen_question):
    print(game_title)
    for counter in range(NUMBER_OF_ROUNDS):
        response, question = func_gen_question()
        print(question)
        answer = input("Your answer: ").lower()
        if (answer != response):
            print(f"'{answer}' is the wrong answer ;(. "
                  f"Correct answer was '{response}'")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
