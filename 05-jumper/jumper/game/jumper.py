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
        for i in range(len(board) - 1):
            comparison += board[i]

        print(comparison)

        if len(self.jumper) < 4:
            can_play = False
            print("\n    x -'Holy crap, you killed Me! You monster! Go to h*ck!' 👻 ")
            print("   /|\\")
            print("   / \\")
            print("\nGame Over! You are officially a _ _ _ _ _\n(The word is loser you loser)")

        elif comparison == word:
            can_play = False
            print("Congradulations")
            print(f"\nGame Over! The word you were looking for was {word}\nYou are officially a _ _ _ _ _\n(That word was loser you loser)")
            

        else:
            self.count += 1

        return can_play

        