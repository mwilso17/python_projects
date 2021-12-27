import matplotlib.pyplot as plt
from random_walk import Randomwalk

# Make a random walk.
rw = Randomwalk()
rw.fill_walk()

# Plot points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()