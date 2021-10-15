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
        self.word = self.list[num - 1]
        for i in range(len(self.word)):
            self.board_display.append("_ ")

    def get_word(self):
        return self.word

    def compare_word(self, guess):
        compare = list(self.word)
        for str in range(len(compare)):
            if guess == self.word[str]:
                self.board_display[str] = guess
                check = True

        return check


    def read_file(self):
        file = open("wordbank.txt", "r")
        self.list = file.readlines()

    