from time import sleep

import raylibpy

from game.score_board import ScoreBoard
from game.word import Word
from game import constants
from game.point import Point


class Director:
    def __init__(self, input_service, output_service):
        self._word = []
        self._input_service = input_service
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._keep_playing = True

    def start_game(self):
        print("Starting game...")
        self._output_service.open_window("Speed")
         
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if self._input_service.window_should_close():
            self._keep_playing = False

        print("Game Over!")

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass
