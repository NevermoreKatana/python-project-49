from brain_games.common.utils import start_game
from brain_games.games.prime import is_prime


def main():
    TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_game(TITLE, is_prime)
