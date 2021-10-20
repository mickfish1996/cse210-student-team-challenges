from game.board import Board
from game.console import Console
from game.player import Player
from game.roster import Roster
from game.move import Move

import random


class Director():
    """
    Director class
    """
    def __init__(self):
        __board = Board
        __console = Console
        __roster = Roster
        __move = Move
        __prepare()

    def start_game():
        print("game")

    def __prepare(self):
        for i in range(2):
            name = self.__roster.read(f"Enter a name for player {i + 1}: ")
            player = player(name)
            self.__console.add_player(player)

    