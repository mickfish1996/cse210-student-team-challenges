from game.actor import Actor
from game import constants

class Word(Actor):
    def __init__(self):
        super().__init__()
        self._point = 0
        self.prepare()

    def prepare(self):
        list_size = len(LIBRARY)
        num = random.randint(1,list_size - 1)
        word = LIBRARY[num]

        self.set_text(word.strip())
        y = random.randint(1, MAX_Y)
        position = Point(MAX_X, y)
        self.set_position(position)
