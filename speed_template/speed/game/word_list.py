import game.constants as constants
from game.word import Word
from game.point import Point
import random

class WordList:
    """ stores words to be used on screen
    type: Info holder
    Attributes:
    self._list_of_words
    
    Methods:
    add_word(self, word)
        Parameters:
            word: string
        Returns:
            void 
    does_contain(self, word)
        Parameters:
            word: string
        Returns:
            boolean 
    delete_word(self, word)
        Parameters:
            word: string
        Returns:
            void 
    """
    def __init__(self):
        self._list_of_words = [None] * constants.MAX_Y
        self._list_of_slots = []
        for i in range(constants.MAX_Y):
            self._list_of_slots.append(i)
        
    def add_word(self):
        #add word onto word_list
        i = self._list_of_slots[random.randint(0,len(self._list_of_slots)-1)]
        self._list_of_slots.remove(i)
        new_word = Word()
        new_word.set_position(Point(random.randint(0, constants.MAX_X), i))
        new_word.set_velocity(Point(random.randint(1,2),0))
        self._list_of_words[i] = new_word

    def does_contain(self,word):
        #checks to see if given word is in the word list. 

        # need to have a something along the lines of self._list_of_words.contains(word) checking to see if it contains the
        # word that we have typed. 
        for a in self._list_of_words:
            if not a == None:
                if(a.get_word() == word):
                    return True

        return False
    
    def delete_word(self,word):
        # delete word from screen
        # need to have a loop that checks the current word to the word that we have in the list currently.
        for x in range(0,constants.MAX_Y):
            if not self._list_of_words[x] == None:
                if self._list_of_words[x].get_word() == word:
                    self._list_of_slots.append(x)
                    self._list_of_words[x] = None

    def get_list(self):
        a = []
        for i in self._list_of_words:
            if not i == None:
                a.append(i)
        return a

# list = WordList()
# list.add_word()
# list.add_word()
# print(list.get_list()[0].get_word())
# word = input()
# print(list.does_contain(word))