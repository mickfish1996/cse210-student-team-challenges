import random

class Board():
    """
    Displays the board and gives the information to Console
    """

    def __init__(self):
        """The class constructor"""
        self._guess = []
        self._hint = []
        self._guess_number = 0
        self.create_number()

    def to_string(self, roster):
        """Converts the board data to string"""
        players = roster.get_players()
        text = ("----------------------")
        text += (f"\nPlayer {players[0].get_name()}: {self._guess}, {self._hint}")
        text += (f"\nPlayer {players[1].get_name()}: {self._guess}, {self._hint}")
        text += ("\n----------------------")
        return text
        
    def create_number(self):
        self.guess_number = random.randint(1000, 9999)
        for i in range(2):
            self._guess[i] = "----"
            self._hint[i] = "****"

    def compare(self, roster):
        player = roster.get_current()
        guess_number = list(self.guess_number)
        guess = list(self._guess[player])
        for i in range(4):
            if guess[i] in guess_number:
                self._hint[player] += "o"
            elif guess[i] == guess_number[i]:
                self._hint[player] += "x"
            else:
                self._hint[player] += "*"

            

    def is_won(self):
        is_won = False
        if self._guess_number == self._guess:
            is_won = True
        return is_won

    def set_guess(self, move, roster):
        player = roster.get_current()
        self._guess = move.get_guess()