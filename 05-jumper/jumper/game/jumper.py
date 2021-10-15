class Jumper:
    def __init__(self):
        self.jumper = []

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

    
    def cut_rope(self):
        self.jumper.pop(0)
            

    def is_alive(self, can_play):
        if len(self.jumper) < 4:
            can_play = False
            print(" x -'Holy crap, you killed Me! You monster! Go to h*ck!'")
            print("/|\\")
            print("/ \\")
            print("\nGame Over! You are officially a _ _ _ _ _\n(The word is loser you loser)")