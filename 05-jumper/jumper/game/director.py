from game.console import Console
from game.board import Board
from game.jumper import Jumper

class Director:

    def __init__(self):
        """The class constructor.
            
            Args:
                self (Director): an instance of Director.
            """
        self.console = Console()
        self.board = Board()
        self.jumper = Jumper()
        self.can_play = True
    
    def start_game(self):
        self.set_board()
        while self.can_play:
            get_inputs()
            do_updates()
            do_outputs()
     
    def get_inputs(self):

        self.console.message

    def do_updates(self):
        pass

    def do_outputs(self):
        pass