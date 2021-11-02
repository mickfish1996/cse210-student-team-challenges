from time import sleep

import raylibpy

from game.score_board import ScoreBoard
from game.word import Word
from game import constants
from game.point import Point
from game.word_input import WordInput
from speed.game import word


class Director:
    def __init__(self, input_service, output_service):
        self._words = []
        self._input_service = input_service
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._keep_playing = True
        self._inputs = WordInput()
        self._make_more = 0
        self._count = 0

    def start_game(self):
        """Begins the game by pulling up the game window"""
        print("Starting game...")
        self._prepare_board()
        self._output_service.open_window("Speed")
 
         
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if self._input_service.window_should_close():
            self._keep_playing = False

        print("Game Over!")

    def _get_inputs(self):
        self._inputs.set_input(self._input_service.get_letter())
        
        
        

    def _do_updates(self):
        """Spawn in new words at random locations 
        on the right side of the screen"""
        self._erase_input()
        self._handle_input_correct
        if self._make_more > 0 and self._count == 20:
            word = Word()
            self._words.append(word)
            self._make_more -= 1
            self._count = 0
        else:
            self._count += 1
        new_count = 0
        for word in self._words:
            word.move_next()
            if word.get_position().get_x() == 0:
                self.destroy_word(new_count)
                new_count += 1
        

    def _do_outputs(self):
        
        self._output_service.clear_screen()

        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._inputs)
        self._output_service.draw_actors(self._words)      
        
        self._output_service.flush_buffer()
        
    def _erase_input(self):
        erase = self._input_service.erase_function()
        if erase == True:
            self._inputs.reset_input()
    

    def _prepare_board(self):
        """Starts the game with 5 words"""
        self._make_more = 5
        self._count = 20
        

    def _handle_input_correct(self):
        pass
    #handle comparison. Give points if it is correct and delete it
        #if (input) = (word):
            #give points and word_input.reset_input
        #if * is input:
            #for i in range(len(word)):
                #self._score_board.add_points(i)
    
    def destroy_word(self,num):
        self._words.pop(num)
        self._make_more += 1
        self._count = 20