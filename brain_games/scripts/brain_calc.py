from brain_games.common.utils import start_game_two_nums
from brain_games.games.calc import check_answer, generate_question, TITLE


def main():
    start_game_two_nums(TITLE, check_answer, generate_question)
