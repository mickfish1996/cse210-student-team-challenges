import random

from raylibpy import set_camera_move_controls
from game.actor import Actor
from game import constants
from game.point import Point

class Word(Actor):
    def __init__(self):
        super().__init__()
        self._point = 0
        self.prepare()
        self.score

    def prepare(self):
        list_size = len(constants.LIBRARY)
        num = random.randint(1,list_size - 1)
        word = constants.LIBRARY[num]

        self.score = len(word)

        self.set_text(word.strip())
        y = random.randint(1, 375)
        x = constants.MAX_X
        position = Point(x, y)
        self.set_position(position)
        velocity = Point(-1,0)
        self.set_velocity(velocity)

    def get_score(self):
        return self.score
        
