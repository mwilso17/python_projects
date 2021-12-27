import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
  # Make a random walk.
  rw = Randomwalk()
  rw.fill_walk()

  # Plot points in the walk.
  plt.style.use('classic')
  fig, ax = plt.subplots()
  ax.scatter(rw.x_values, rw.y_values, s=15)
  plt.show()

  keep_running = input('Make another walk? (y/n): ')
  if keep_running == 'n':
    break