from brain_games import cli
from .brain_games import greeting
from brain_games.common.logic import play_game
from brain_games.games.even import is_even


def main():
    TITLE = 'Answer "yes" if the number is \
even, otherwise answer "no".'
    greeting()
    name = cli.welcome_user()
    play_game(name, TITLE, is_even)
