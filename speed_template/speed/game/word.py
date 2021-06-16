from game.actor import Actor
import game.constants as constants
import random


class Word(Actor):
    """Verify if the word typed matches 

    Stereotype:
        Information Holder

    Attributes:
        _user_word_typed (?) (string): The sequence of letters typed by the user
    """

    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of Word.
            word (string)
        
        """
        super().__init__()
        i = random.randint(0, len(constants.LIBRARY))

        self._word = constants.LIBRARY[i]
        super().set_text(self._word)

        

    def equals(self, word):
        """Whether this Word is equal to the word randomly chosen.

        Args:
            self (Word): An instance of Word.
            word (Word): The Word to compare.

        Returns: 
            boolean: True if both word and randword are equal; false if otherwise.
        """
        return self._word == word

    def get_word(self):
        """Gets the random word.
        
        Args:
            self (Word): An instance of Word.
            
        Returns:
            string: A chosen word.
        """
        
        return self._word