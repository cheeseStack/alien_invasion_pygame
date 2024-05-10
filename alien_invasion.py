# first file, page 229
import sys

import pygame

from settings import Settings


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """
    
    def __init__(self):
        """ Initialise the game, and create the resources """
        pygame.init()
        
        # import the settings from settings.py
        self.settings = Settings()
        
    def run_game(self):
        """ Start the main loop of the game """ 
        pygame.init()
        while True:
           
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Use the bg_color - redraw the screen during each pass of the loop.;
            self.screen.fill(self.settings.bg_color)
                    
            # Make the most recently drawn screen still visible
            pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game
    
    ai = AlienInvasion()
    ai.run_game()