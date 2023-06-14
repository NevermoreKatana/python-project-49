from brain_games.common.utils import start_game
from brain_games.games.calc import generate_question, TITLE


def main():
    start_game(TITLE, generate_question)
