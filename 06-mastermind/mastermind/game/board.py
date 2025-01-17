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
        guess = self._guess
        text = ("----------------------")
        text += (f"\nPlayer {players[0].get_name()}: {guess[0]}, {self._hint[0]}")
        text += (f"\nPlayer {players[1].get_name()}: {guess[1]}, {self._hint[1]}")
        text += ("\n----------------------")
        return text
        
    def create_number(self):
        """Generates a random number"""
        self._guess_number = random.randint(1000, 9999)
        for i in range(2):
            self._guess.append("----")
            self._hint.append("****")

    def compare(self, roster):
        """Compares a guess to the randomly generated number"""
        player = roster.get_current_player()
        guess_number = list(str(self._guess_number))
        guess = list(str(self._guess[player]))
        self._hint[player] = ""
        for i in range(4):
            if guess[i] == guess_number[i]:
                self._hint[player] += "x"
            elif guess[i] in guess_number:
                self._hint[player] += "o"
            else:
                self._hint[player] += "*"

    def is_won(self, roster):
        """Determines if a player has"""
        player = roster.get_current_player()
        is_won = False
        if self._guess_number == self._guess[player]:
            is_won = True
        return is_won

    def set_guess(self, move, roster):
        player = roster.get_current_player()
        self._guess[player] = move.get_guess()

        
    def set_word(self, list):
        num = random.randint(0, len(list))
        word = list[num - 2]
        return word