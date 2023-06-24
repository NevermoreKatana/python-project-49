#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brain_games.game_utilities.utils import start_game, initialize_game
from brain_games.games.progression import TITLE, create_expression


def main():
    name = initialize_game()
    start_game(name, TITLE, create_expression)
