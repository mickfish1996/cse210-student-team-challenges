
class Console:
    def __init__(self):
        pass

    def board_out(self, board):
        for i in range(len(board) - 1):
            print(board[i], end = "")

        print("\n")

    def jumper_out(self,jumper):
        for i in range(len(jumper)):
            print(jumper[i])

    def prompt_user(self):
        user_input = input("Guess a letter😊 [a-z]: ")
        print()
        return user_input