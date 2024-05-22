# first file, page 229
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """
    
    def __init__(self):
        """ Initialise the game, and create the resources """
        pygame.init()
        
        # import the settings from settings.py
        self.settings = Settings()
        
        # small screen mode:
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # full screen mode:
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        
        # Load the ship
        self.ship = Ship(self)
        
        # Create the bullets group
        self.bullets = pygame.sprite.Group()
        
        
        
        
    def run_game(self):
        """ Start the main loop of the game """ 
        pygame.init()
        while True:
            # _check_events helper method
            self._check_events()
            
            # call the ship update method to track for movement flags
            # update the ship's position before drawing to the screen in _update_screen
            self.ship.update()
            
            # Update the bullets position
            self._update_bullets()
            
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
            # Responding to a key press, p238
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)
                
                
      
    # refactor code for keydown events, p244 
    def _check_keydown_events(self, event): 
        if event.key == pygame.K_RIGHT: # move right
             # Move the ship to the right
            self.ship.moving_right = True     
        elif event.key == pygame.K_LEFT: # move left
            self.ship.moving_left = True  
        elif event.key == pygame.K_q: # quit
            sys.exit()
        elif event.key == pygame.K_SPACE: # fire bullets, p249
            self._fire_bullet()
        
            
    # helper function for KEYUP events
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   
            
    
    # helper method to fire bullets, p249
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group"""
        # limit bullets to bullets_allowed setting
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
         
                
    # Helper method to update screen
    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
         
        # Use the bg_color - redraw the screen during each pass of the loop.;
        self.screen.fill(self.settings.bg_color)
            
        # Run an instance of the ship
        self.ship.blitme()
        
        # display all the bullets in self.bullets property
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        # Make the most recently drawn screen still visible
        pygame.display.flip()
        
    # helper method for updating bullets
    def _update_bullets(self):
        """ Update the position of the bullets and remove old bullets """
        # Update bullet position
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


            

if __name__ == '__main__':
    # Make a game instance, and run the game
    
    ai = AlienInvasion()
    ai.run_game()