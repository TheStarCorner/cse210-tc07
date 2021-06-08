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
        position = Point(-1, 0) # or (0, -1)?
        self.set_position(position)
        self.set_text(f"Buffer: {self._letter}")
    
    def add_letter(self, letter):
        letter = ""
        self._letter.append(letter)
        
    def get_word(self):
        return self.word