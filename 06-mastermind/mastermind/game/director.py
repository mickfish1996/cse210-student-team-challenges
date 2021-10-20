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
        self.__board = Board
        self.__console = Console
        self.__roster = Roster
        self.__move = Move
        

    def start_game():
        self.__prepare()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            

    def __prepare(self):
        for i in range(2):
            name = self.__roster.read(f"Enter a name for player {i + 1}: ")
            player = player(name)
            self.__console.add_player(player)

    def _get_inputs(self):
        players = self.__roster.get_players()
        board = self._board.to_string(players)