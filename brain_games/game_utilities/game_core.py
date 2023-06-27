from brain_games.scripts.brain_games import greeting
from brain_games.game_utilities.games_engine import play_game
import prompt


def initialize_game():
    greeting()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def start_game(title: str, func):
    name = initialize_game()
    play_game(name, title, func)
