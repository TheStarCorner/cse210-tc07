from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):
    screen.print_at("Test", 20, 20, 7)
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

Screen.wrapper(main)