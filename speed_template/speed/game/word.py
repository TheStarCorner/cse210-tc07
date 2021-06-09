import random
from game.actor import Actor
from game.point import Point
from game.word_list import WordList

import game.constants
import random


class Word(Actor):
    """Verify if the word typed matches 

    Stereotype:
        Information Holder

    Attributes:
        _user_word_typed (?) (string): The sequence of letters typed by the user
    """
    

    def __init__(self, word):

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of Word.
        
        """


        word = constants.LIBRARY#needs to be fixed

        self._word = word
        

    def equals(self, other):
        """Whether this Word is equal to the word randomly chosen.

        Args:
            self (Word): An instance of Word.
            other (Word): The Word to compare.

        Returns: 
            boolean: True if both word and randword are equal; false if otherwise.
        """

        return self._word == other.get_randword()

    def get_randword(self):

        return self._word == other.get_word()

    def get_word(self):

        """Gets the random word.
        
        Args:
            self (Word): An instance of Word.
            
        Returns:
            string: A chosen word.
        """
        

        return self._randword

        return self._word



 