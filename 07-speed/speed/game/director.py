from time import sleep

import raylibpy

from game.score_board import Score_board
from game.word import Word
from game import constants
from game.point import Point


class director:
    def __init__(self, input_service, output_service):
        self._word = []
        self._input_service = input_service
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._keep_playing = True
