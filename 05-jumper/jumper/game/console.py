
class Console:
    def __init__(self):
        pass
    
    # This function will display the board display value
    def board_out(self, board):
        for i in range(len(board) - 1):
            print(board[i], end = "")

        print("\n")
    
    # This function will display the jumper
    def jumper_out(self,jumper):
        for i in range(len(jumper)):
            print(jumper[i])

        print("\n")
    
    # This function will prompt the user for their guess.
    def prompt_user(self):
        user_input = input("Guess a letter😊 [a-z]: ")
        print()
        return user_input