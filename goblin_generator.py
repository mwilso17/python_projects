# Mike Wilson 22 June 2021
# This program generates a low-level 'goblin' monster to be used in a
# table top style RPG. Imports from the Python standard library.

from random import randint

class Goblin:
  """Represents a low level 'goblin' monster that has 3-9 HP."""

  def __init__(self, hit_points):
    """Initializes attributes."""
    self.hit_points = hit_points

  def create_goblin(self):
    """Simulate the creation of a low level 'goblin'"""
    return randint(3, 9)