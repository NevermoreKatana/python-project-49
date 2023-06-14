from brain_games.scripts.brain_games import main
from brain_games.common.logic import play_game, play_game_two_numbers



def start_game(title: str, func):
    name = main()
    play_game(name, title, func)


def start_game_two_nums(title: str, func, func1):
    name = main()
    play_game_two_numbers(name, title, func, func1)
