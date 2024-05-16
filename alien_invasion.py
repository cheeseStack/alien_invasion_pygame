# first file, page 229
import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """
    
    def __init__(self):
        """ Initialise the game, and create the resources """
        pygame.init()
        
        # import the settings from settings.py
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        
    def run_game(self):
        """ Start the main loop of the game """ 
        pygame.init()
        while True:
            # _check_events helper method
            self._check_events()
            
            # _update_screen helper method
            self._update_screen()
           
        
            
            
    
    # Helper methods, with leading underscore 
    # Create a _check_events helper method, p236
    def _check_events(self):
        # Watch for keyboard and mouse 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
    # Helper method to update screen
    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
        
        # Use the bg_color - redraw the screen during each pass of the loop.;
        self.screen.fill(self.settings.bg_color)
            
        # Run an instance of the ship
        self.ship.blitme()
                    
        # Make the most recently drawn screen still visible
        pygame.display.flip()

            

if __name__ == '__main__':
    # Make a game instance, and run the game
    
    ai = AlienInvasion()
    ai.run_game()