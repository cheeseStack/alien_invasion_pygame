# first file, page 229
import sys

import pygame


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """
    
    def __init__(self):
        """ Initialise the game, and create the resources """
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        # ~ Set the background color, p231
        self.bg_color = (230, 230, 230)
        
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
            self.screen.fill(self.bg_color)
                    
            # Make the most recently drawn screen still visible
            pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game
    
    ai = AlienInvasion()
    ai.run_game()