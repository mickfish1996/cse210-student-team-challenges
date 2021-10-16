from game.dealer import Dealer
class Director:
    
    
    def __init__(self):
        """The class constructor.

        Args:
            self(Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.guess = 0
        self.last_card = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): in instance of Director.
        """
        while self.keep_playing:
            self.do_outputs()
    
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means drawing the dice

        Args:
            self (Director: An instance of Director.)        
        """
        self.dealer.draw_card()
        

    def do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points(self.guess, self.last_card)
        self.score += points

    def display_first_card(self):
        """Displays the first card of the game"""
        value = self.dealer.card
        if value < 11:
            print(f"The card is: {value}")
        elif value == 11:
            print("The card is: Jack")
        elif value == 12:
            print("The card is: Queen")
        elif value == 13:
            print("The card is: King")

    def display_second_card(value):
        """Displays the second card of the game"""
        if value < 11:
            print(f"Next card was: {value}")
        elif value == 11:
            print("Next card was: Jack")
        elif value == 12:
            print("Next card was: Queen")
        elif value == 13:
            print("Next card was: King")

    def do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means the card that was drawn and the score.

        Args:
            self(Director): An instance of Director.
        """
        if self.dealer.num_draws == 0:
            self.get_inputs()
        self.display_first_card()
        self.guess = input(f"Higher or Lower? [h/l] ")
        self.last_card = self.dealer.card
        self.get_inputs()
        self.do_updates()
        #print(f"Next card was: {self.dealer.card}")
        self.display_first_card()
        print(f"Your score is: {self.score}")


        if self.score <= 0:
            print("Game over!")
            self.keep_playing = False

        else:
            choice = input("Keep playing? [y/n] ")

        if self.score > 0 and choice == "y":
            self.keep_playing = True
            
            
        else:
            self.keep_playing = False