from brain_games import cli
from .brain_games import greeting
from brain_games.games.gcd import nod_game


def main():
    greeting()
    name = cli.welcome_user()
    nod_game(name)
