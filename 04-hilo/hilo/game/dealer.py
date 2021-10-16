# Dealer Class File

import random
class Dealer:
    def __init__(self):
        """
        """
        self.card = 0
        self.num_draws = 0
        
    def can_draw(self, points):
        """
        """
        if points <= 0:
            return True


    def get_points(self, guess, last_card):
        """ Will take away points or award points depending on the guess
        the accuracy of their guess
        """
        if guess == "h" and last_card <= self.card:
            return 100
        elif guess == "l" and last_card >= self.card:
            return 100
        elif guess == "h" and last_card > self.card:
            return -75
        elif guess == "l" and last_card < self.card:
            return -75

        
    def draw_card(self):
        """
        """
        result = random.randint(1, 13)
        self.card = result
        self.num_draws += 1