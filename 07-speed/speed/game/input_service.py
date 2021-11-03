import sys
import raylibpy

from game.word_input import WordInput

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._inputs = WordInput()
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        self.erase = False
        event = raylibpy.get_key_pressed()
        if self._is_enter_pressed():
            event = 13
        elif self._is_esc_pressed():
            event = 27
        assert type(event) is int
        
        if not event is None:
            if event == 27 or event == 96:
                sys.exit()
            elif event == 92 or event == 13: 
                result = "*"
                self.erase = True
            elif event >= 97 and event <= 122: 
                result = chr(event)
                assert type(result) is str
            #self.erase_function()
        return result

    def erase_function(self):
        return self.erase

    def _is_enter_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_ENTER)

    def _is_esc_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_ESCAPE)