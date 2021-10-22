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
        self.__board = Board()
        self.__console = Console()
        self.__roster = Roster()
        self.__move = None
        self._keep_playing = True
        

    def start_game(self):
        self.__prepare()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            

    def __prepare(self):
        
        for i in range(2):
            name = self.__console.read(f"Enter a name for player {i + 1}: ")
            player = Player(name)
            self.__roster.add_player(player)

    def _get_inputs(self):
        # displays the current board
        board = self.__board.to_string(self.__roster)
        self.__console.write(board)
        # gets input from the user
        player = self.__roster.get_current()
        self.__console.write(f"{player.get_name()}'s turn:")
        guess = self.__console.read_number("What is your Guess? ")
        move = Move(guess)
        player.set_move(move)

    def _do_updates(self):
        player = self.__roster.get_current()
        move = player.get_move()
        self.__board.set_guess(move, self.__roster)
        self.__board.compare(self.__roster)

    def _do_outputs(self):
        if self.__board.is_won():
            winner = self.__roster.get_current()

        self.__roster.next_player()

        
        