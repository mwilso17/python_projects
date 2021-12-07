import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  '''A class to represent a single alien in the fleet'''

  def __init__(self, ai_game):
    '''Initialize the alien and set its starting point'''
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings

    # Load alien image and set its rect attribute
    self.image = pygame.image.load('alien_invasion\images\ship_alien.bmp')
    self.rect = self.image.get_rect()

    # Start each new alien near the top left of the screen.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # Store alien's exact horizontal position
    self.x = float(self.rect.x)

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
      return True

  def update(self):
    self.x += (self.settings.alien_speed * self.settings.fleet_direction)
    self.rect.x = self.x