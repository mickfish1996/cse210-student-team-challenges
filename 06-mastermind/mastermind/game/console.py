
class Console():
    """
    Console class
    """
    
    # Let user input names for the each of the 2 players
    def read(self,prompt):
        return input(prompt)

    # Displays the board
    def display_board(self,text):
        print(text)

    # prompt for the user input.
    def read_number(self, prompt):
        return int(input(prompt))