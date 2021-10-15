
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
<<<<<<< HEAD
        user_input = input("Adivina una letra [a-z]: ")
=======
        user_input = input("Guess a letter😊 [a-z]: ")
>>>>>>> 56d7372a01c04f1f21ad91b7df90cd4493ddfd93
        return user_input