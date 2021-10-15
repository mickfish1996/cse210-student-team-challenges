import random

class Board():

    def __init__(self):
        self.word = ""
        self.board_display = ""
        self.filename = ""
        self.list = []
        
    
    def set_word(self):
        num = random.randint(0, len(self.list))
        self.word = self.list[num]

    def get_word(self):
        return self.word

    def compare_word(self):
        pass

    def read_file(self):
        file = open("wordbank.txt", "r")
        self.list = file.readlines()

    def display_board():
        for i in range(len(self.word)):
            pass
            
