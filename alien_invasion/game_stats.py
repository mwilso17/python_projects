class GameStats:
  '''tracks stats for Alien Invasion'''

  def __init__(self, ai_game):
    self.settings = ai_game.settings
    self.reset_stats()

    # Start game in inactive state
    self.game_active = False

  def reset_stats(self):
    self.ships_left = self.settings.ship_limit