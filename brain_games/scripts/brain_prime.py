from brain_games.common.utils import start_game
from brain_games.games.prime import is_prime, TITLE


def main():
    start_game(TITLE, is_prime)
