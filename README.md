# Проект "Игры разума" 


## Описание
«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

Калькулятор. Арифметические выражения, которые необходимо вычислить
Прогрессия. Поиск пропущенных чисел в последовательности чисел
Определение четного числа
Определение наибольшего общего делителя
Определение простого числа


## Установка игр сразу в систему

```sh
make install
```
```sh
make build
```
```sh
make package-install
```

## Usage

```sh
brain-calc   
brain-even   
brain-games  
brain-nod    
brain-prime  
brain-prog
```

## Древо проекта

├── Makefile
├── README.md
├── brain_games
│   ├── __init__.py
│   ├── cli.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── logic.py
│   │   └── utils.py
│   ├── games
│   │   ├── __init__.py
│   │   ├── calc.py
│   │   ├── even.py
│   │   ├── gcd.py
│   │   ├── prime.py
│   │   └── progression.py
│   └── scripts
│       ├── __init__.py
│       ├── brain_calc.py
│       ├── brain_even.py
│       ├── brain_games.py
│       ├── brain_gcd.py
│       ├── brain_prime.py
│       └── brain_progression.py
├── poetry.lock
├── pyproject.toml
└── setup.cfg


### Hexlet tests and linter status:
[![Actions Status](https://github.com/NevermoreKatana/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/NevermoreKatana/python-project-49/actions)
<a href="https://codeclimate.com/github/NevermoreKatana/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/4517940bc5185bb713bc/maintainability" /></a>
[![asciicast](https://asciinema.org/a/1jWbJf3CtATV6J83wMZ9yNtRr.svg)](https://asciinema.org/a/1jWbJf3CtATV6J83wMZ9yNtRr)

[![asciicast](https://asciinema.org/a/1jWbJf3CtATV6J83wMZ9yNtRr.svg)](https://asciinema.org/a/nPyJQegmeADdVpjXUpqmQ3eSk)

[![asciicast](https://asciinema.org/a/Hp2Y5GbePcktTveSaPyxCLXOK.svg)](https://asciinema.org/a/Hp2Y5GbePcktTveSaPyxCLXOK)

[![asciicast](https://asciinema.org/a/Hp2Y5GbePcktTveSaPyxCLXOK.svg)](https://asciinema.org/a/eKs7SF06idIsbkV5dFJuJ56Hh)

[![asciicast](https://asciinema.org/a/XloWgAMzZ3PAp9u4Ay1VCQvah.png)](https://asciinema.org/a/XloWgAMzZ3PAp9u4Ay1VCQvah)
