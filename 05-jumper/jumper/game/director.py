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
        self.board.read_file()
        self.board.set_word()
        while self.can_play:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
     
    def get_inputs(self):
        self.guess = self.console.prompt_user()

    def do_updates(self):
        self.word.compare_word(self.guess)

    def do_outputs(self):
        self.console.board_out(self.board.display_board)
        self.console.jumper_out(self.jumper.get_jumper())

        self.jumper.is_alive(self.can_play)