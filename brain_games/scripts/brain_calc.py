#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brain_games.common.utils import start_game
from brain_games.games.calc import create_expression, TITLE


def main():
    start_game(TITLE, create_expression)
