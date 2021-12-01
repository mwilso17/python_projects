import pygame

class Ship:
  '''A class to manage the ship'''

  def __init__(self, ai_game):
    ''''Initialize the ship and set its starting point'''
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # Load the ship image and get its rect.
    self.image = pygame.image.load('alien_invasion\images\ship.bmp')
    self.rect = self.image.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom

  def blitme(self):
    self.screen.blit(self.image, self.rect)