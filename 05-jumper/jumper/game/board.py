import random
from game.jumper import Jumper
class Board():

    def __init__(self):
        self.word = ""
        self.board_display = []
        self.filename = ""
        self.list = []
        self.jumper = Jumper
        
    # This method will get the word to use from a list
    # that is read in
    def set_word(self):
        num = random.randint(0, len(self.list))
        self.word = self.list[num - 2]
        for i in range(len(self.word)):
            self.board_display.append("_ ")
    
    # This funciton will return a word to be used
    def get_word(self):
        return self.word

    # This function will see if your guess is correct.
    def compare_word(self, guess):
        compare = list(self.word)
        check = False
        for str in range(len(compare)):
            if guess == self.word[str]:
                self.board_display[str] = guess
                check = True

        return check

    # This method will read the file
    def read_file(self):
        file = open("wordbank.txt", "r")
        self.list = file.readlines()

    