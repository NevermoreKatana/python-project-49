from brain_games import cli
from .brain_games import greeting
from brain_games.games.prime import is_prime
from brain_games.common.logic import play_game


def main():
    TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    greeting()
    name = cli.welcome_user()
    play_game(name, TITLE, is_prime)
