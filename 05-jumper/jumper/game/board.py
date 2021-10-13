

class Board():

    def __init__(self):
        self.word = ""
        self.board_display = ""
        self.filename = ""
        self.list = []
        
    
    def set_word(self):
        pass

    def get_word(self):
        return self.word

    def compare_word(self):
        pass

    def read_file(self):
        self.list = open("wordbank.txt", "r")

    def display_board():
        pass