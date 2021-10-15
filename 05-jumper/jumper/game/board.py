import random
from game.jumper import Jumper
class Board():

    def __init__(self):
        self.word = ""
        self.board_display = []
        self.filename = ""
        self.list = []
        self.jumper = Jumper
        
    
    def set_word(self):
        num = random.randint(0, len(self.list))
        self.word = self.list[num]
        for i in range (len(self.word)):
            self.board_display.append("_ ")

    def get_word(self):
        return self.word

    def compare_word(self, guess):
        for str in self.word:
            if guess == self.word:
                self.display_board = guess
            else:
                self.jumper.cut_rope()


    def read_file(self):
        file = open("wordbank.txt", "r")
        self.list = file.readlines()

    def display_board(self):
        for i in range(len(self.word)):
            pass