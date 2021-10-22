
class Move():
    """
    Move class. 
    """

    # Initialization
    def __init__(self, guess):
        self._guess = guess
    
    # Access prviate variable guess
    def get_guess(self):
        return self._guess
        