class Jumper:
    def __init__(self):
        self.jumper = []

    def set_jumper(self):
        self.jumper = [
        "   ___",
        "  /___\\",
        "  \   /",
        "   \ /",
        "    0",
        "   /|\\",
        "   / \\"
        ]   

    
    def cut_rope(self):
        pass
        rope = 4
        rope -= 1
        if rope == 0:
            print(" x -'Holy crap, you killed Me! You monster! Go to h*ck!'")
            print("/|\\")
            print("/ \\")

    def is_alive(self, can_play):
        if len(self.jumper) < 4:
            can_play = False
        pass