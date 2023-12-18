#!/usr/bin/env python3


from brain_games.logic import start
from brain_games.games import game_gcd


def main():
    start(game_gcd)

if __name__ == '__main__':
    main()