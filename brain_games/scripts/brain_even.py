from brain_games.common.utils import start_game
from brain_games.games.even import is_even


def main():
    TITLE = 'Answer "yes" if the number is \
even, otherwise answer "no".'
    start_game(TITLE, is_even)
