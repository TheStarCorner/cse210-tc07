from actor import Actor
import constants
import random


import constants
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
        
        i = random.randint(0, len(constants.LIBRARY))

        word = constants.LIBRARY[i]
        self._word = word

        

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

a = Word()
