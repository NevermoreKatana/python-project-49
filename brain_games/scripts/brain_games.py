from brain_games.cli import welcome_user


def greeting():
    print('Welcome to the Brain Games!')


def main():
    greeting()
    name = welcome_user()
    return name