class WordInput():
    def __init__(self):
        self._input = ""


    def get_input(self):
        return f"Text input: {self._input}"

    def set_input(self, inputs):
        self._input += inputs

    def reset_input(self):
        self.input = ""