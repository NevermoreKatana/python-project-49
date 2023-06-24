#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brain_games.game_utilities.utils import start_game
from brain_games.games.gcd import TITLE, create_expression
from brain_games import cli


def main():
    name = cli.welcome_user()
    start_game(name, TITLE, create_expression)
