
class Console:
    def __init__(self):
        pass

    def board_out(self, board):
        for i in range (len(board)):
            print(board[i], end = "")

    def jumper_out(self,jumper):
        for i in range (len(jumper)):
            print(jumper[i])

    def prompt_user(self):
        user_input = input("Adivina una letra [a-z]: ")
        return user_input