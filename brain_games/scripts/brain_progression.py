from brain_games import cli
from brain_games.scripts.brain_games import greeting
from brain_games.games.progression import prog_game


def main():
    greeting()
    name = cli.welcome_user()
    prog_game(name)
