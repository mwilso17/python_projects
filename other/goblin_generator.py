# Mike Wilson 22 June 2021
# This program generates a low-level 'goblin' monster to be used in a
# table top style RPG. Imports from the Python standard library.

from random import randint

class Goblin:
  """Represents a low level 'goblin' monster that has 3-9 HP."""

  def __init__(self, hit_points=3):
    """Initializes attributes."""
    self.hit_points = hit_points

  def create_goblin(self):
    """Simulate the creation of a low level 'goblin'"""
    return randint(3, 9)


# Make a goblin.
goblin_a = Goblin()

hp = []
for roll_num in range(1):
  health = goblin_a.create_goblin()
  hp.append(health)

print(f"\nA goblin has been created and has {hp} hitpoints: ")
