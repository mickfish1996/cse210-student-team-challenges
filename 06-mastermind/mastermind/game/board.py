import random

class Board():
    """
    Displays the board and gives the information to Console
    """

    def __init__(self):
        """The class constructor"""
        _guess = "----"
        _hing = "****"

    def to_string(self, roster):
        """Converts the board data to string"""
        text = ("----------------------")
        text += (f"Player {roster.[0]}: {self._guess}, {self._hing}")
        text += (f"Player {roster.[1]}: {self._guess}, {self._hing}")
        text += ("----------------------")
        text += (f"{Roster.get_current}'s turn:")
        return text
        
    def create_number(self):
        guess_number = random.randint(1000, 9999)