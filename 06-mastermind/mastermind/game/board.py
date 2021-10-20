class Board():
    """
    Displays the board and gives the information to Console
    """

    def __init__(self):
        """The class constructor"""
        pass

    def to_string(self):
        """Converts the board data to string"""
        text = ("----------------------")
        text += ("Player {Player variable}: ----, ****")
        text += ("Player {Player variable}: ----, ****")
        text += ("----------------------")
        text += ("{Player variable}'s turn:")
        return text
        
    