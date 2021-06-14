from game.input_service import InputService
from game.output_service import OutputService
from time import sleep
from game.buffer import Buffer
from game.score import Score
from game.word_list import WordList
from game.word import Word
import game.constants as constants

class Director:
    def __init__(self, input_service, output_service):
        self._input_service = input_service
        self._output_service = output_service
        self._keep_playing = True
        self._word_list = WordList()
        self._word_list.add_word()
        self._word_list.add_word()
        self._word_list.add_word()
        self._word_list.add_word()
        self._word_list.add_word()
        self._score = Score()
        self._buffer = Buffer()
    
    def start_game(self):
        while self._keep_playing:
            self._do_updates(self._get_inputs())
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
    
    def _get_inputs(self):
        letter = self._input_service.get_letter()
        return letter
    
    def _do_updates(self, letter):
        if letter == '*':
            word = self._buffer.get_word()
            self._buffer.clear_buffer()
            if self._word_list.does_contain(word):
                self._word_list.delete_word(word)
        else:
            self._buffer.add_letter(letter)
        for things in self._word_list.get_list():
            things.move_next() #moves all the words to their next place
    
    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._word_list.get_list())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()