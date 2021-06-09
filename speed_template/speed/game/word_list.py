from game import word

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
        self._list_of_words = [word]



    def add_word(self):
        #add word onto word_list
        self._list_of_words.append(Word())


    def does_contain(self,word):
        #checks to see if given word is in the word list. 

        # need to have a something along the lines of self._list_of_words.contains(word) checking to see if it contains the
        # word that we have typed. 
        if self._list_of_words.contains(word):
            return True

        else: return False
    
    def delete_word(self,word):
        #delete word from screen
        # need to have a loop that checks the current word to the word that we have in the list currently.
        if self.word == self._list_of_words.contains(word):
            self._list_of_words.remove(word)
        else:
           # do nothing you idiot computer