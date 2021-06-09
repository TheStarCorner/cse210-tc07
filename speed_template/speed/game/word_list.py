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
        self._list_of_words = word 


    def add_word(self, word):
        #add word onto word_list
        self._list_of_words.append(word)


    def does_contain(self,word):
        #checks to see if given word is in the word list.
        if word == word:
            return True

        else: return False
    
    def delete_word(self,word):
        #delete word from screen
        self._list_of_words.remove(word)