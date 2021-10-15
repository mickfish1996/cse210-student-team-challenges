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
        self.guess = 0
        self.board = Board()
        self.jumper = Jumper()
        self.can_play = True


    
    def start_game(self):
        self.set_board()
        while self.can_play:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
     
    def get_inputs(self):
        self.guess = self.console.prompt_user()

    def do_updates(self):
        self.jumper.cut_rope()

    def do_outputs(self):
        

        self.jumper.is_alive(self.can_play)