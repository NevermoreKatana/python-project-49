from brain_games import cli
from brain_games.scripts.brain_games import greeting
from brain_games.common.logic import play_game


def initialize_game():
    greeting()
    name = cli.welcome_user()
    return name


def start_game(title: str, func):
    name = initialize_game()
    play_game(name, title, func)
