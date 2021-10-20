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


    # this will initialize all the word and the jumper and will run the loop
    def start_game(self):
        self.board.read_file()
        self.board.set_word()
        self.jumper.set_jumper()
        while self.can_play:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    # This function will prompt the user
    def get_inputs(self):
        if self.jumper.count == 0:
            self.console.jumper_out(self.jumper.get_jumper())
        self.guess = self.console.prompt_user()
    
    # This function will update the board display and will decide
    # if the rope gets cut.
    def do_updates(self):
        comparison = self.board.compare_word(self.guess)
        if comparison == True:
            pass

        else:    
            self.jumper.cut_rope()

    # This function will display to the user and decide if the 
    # game should keep going
    def do_outputs(self):
        self.console.board_out(self.board.board_display)
        self.can_play = self.jumper.is_alive(self.can_play,self.board.board_display,self.board.word)
        if self.can_play:
            self.console.jumper_out(self.jumper.get_jumper())