import random

class Board():
    """
    Displays the board and gives the information to Console
    """

    def __init__(self):
        """The class constructor"""
        self._guess = "----"
        self._hing = "****"

    def to_string(self, roster):
        """Converts the board data to string"""
        players = roster.get_players()
        text = ("----------------------")
        text += (f"\nPlayer {players[0].get_name()}: {self._guess}, {self._hing}")
        text += (f"\nPlayer {players[1].get_name()}: {self._guess}, {self._hing}")
        text += ("\n----------------------")
        return text
        
    def create_number(self):
        guess_number = random.randint(1000, 9999)