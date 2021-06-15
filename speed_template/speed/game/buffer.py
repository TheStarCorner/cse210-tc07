import random
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        position = Point(1, 20)
        self.set_position(position)
        self._word = ""
        self.set_text (f"Buffer: {self._word}")
    
    def add_letter(self, letter):
        self._word = self._word + str(letter)
        self.set_text(f"Buffer: {self._word}")

        # self._letter.append(letter)

    def clear_buffer(self):
        self._word = "*"
        self.set_text (f"Buffer: {self._word}")

        
    def get_word(self):
        return self._word