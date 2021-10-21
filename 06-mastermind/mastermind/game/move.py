
class Move():
    """
    Move class. 
    """
    def __init__(self, guess):
        self._guess = guess
    
    def get_move(self):
        return self._guess
        