from brain_games import cli
from ..scripts.brain_games import greeting
from .logic import play_game, play_game_two_numbers


def initialize_game():
    greeting()
    name = cli.welcome_user()
    return name


def start_game(title: str, func):
    name = initialize_game()
    play_game(name, title, func)


def start_game_two_nums(title: str, func, func1):
    name = initialize_game()
    play_game_two_numbers(name, title, func, func1)
