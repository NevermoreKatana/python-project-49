from brain_games.common.utils import start_game
from brain_games.games.even import is_even, TITLE


def main():
    start_game(TITLE, is_even)
