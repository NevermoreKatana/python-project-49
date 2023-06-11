from brain_games import cli
from .brain_games import greeting
from brain_games.common.logic import play_game_two_numbers
from brain_games.games.calc import generate_question, check_answer


def main():
    TITLE = 'What is the result of the expression?'
    greeting()
    name = cli.welcome_user()
    play_game_two_numbers(name, TITLE, check_answer, generate_question)
