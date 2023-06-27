#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brain_games.game_utilities.game_core import start_game
from brain_games.games.prime import TITLE, create_expression


def main():
    start_game(TITLE, create_expression)
