from brain_games.common.utils import start_game
from brain_games.games.even import TITLE, generate_question


def main():
    start_game(TITLE, generate_question)
