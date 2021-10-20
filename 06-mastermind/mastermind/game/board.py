import random

class Board():
    """
    Displays the board and gives the information to Console
    """

    def __init__(self):
        """The class constructor"""
        _guess = "----"
        _hing = "****"

    def to_string(self):
        """Converts the board data to string"""
        text = ("----------------------")
        text += (f"Player {Player variable}: {}, {}")
        text += (f"Player {Player variable}: {}, {}")
        text += ("----------------------")
        text += ("{Player variable}'s turn:")
        return text
        
    def create_number(self):
        guess_number = random.randint(1000, 9999)