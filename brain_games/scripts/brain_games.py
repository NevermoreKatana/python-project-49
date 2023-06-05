from brain_games import cli
from .brain_even import parity_check_game


def greeting():
    print('Welcome to the Brain Games!')


def main():
    greeting()
    name = cli.welcome_user()
    parity_check_game(name)


if __name__ == '__main__':
    main()
