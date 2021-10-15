class Jumper:
    def __init__(self):
        self.jumper = []
        self.count = 0

    def set_jumper(self):
        self.jumper = [
        "   ___",
        "  /___\\",
        "  \\   /",
        "   \\ /",
        "    0",
        "   /|\\",
        "   / \\"
        ]   

    def get_jumper(self):
        return self.jumper
        
    def cut_rope(self):
        self.jumper.pop(0)
            

    def is_alive(self, can_play,board,word):
        comparison = ""
        for i in range(len(board)):
            comparison += board[i]

        if len(self.jumper) < 4:
            can_play = False
            print("\n    x -'Holy crap, you killed Me! You monster! Go to h*ck!' 👻 ")
            print("   /|\\")
            print("   / \\")
            print("\nGame Over! You are officially a _ _ _ _ _\n(The word is loser you loser)")

        elif board == word:
            can_play = False
            print("Congradulations")
            

        else:
            self.count += 1

        return can_play

        