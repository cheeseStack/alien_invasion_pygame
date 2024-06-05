# page 257
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """
    
    def __init__(self, ai_game):
        """ Initialise the alien and its starting position """
        super().__init__()    
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute.
        alien_2 = pygame.image.load('images/alien_2.bmp')
        alien_2 = pygame.transform.scale(alien_2, (60, 107))
        self.image = alien_2
        self.rect = self.image.get_rect()
        
        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.width
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)