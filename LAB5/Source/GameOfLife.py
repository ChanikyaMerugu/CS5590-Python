import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

K = 150
ON = 255
OFF = 0
vals = [ON, OFF]

#  random on/off
grid = np.random.choice(vals, K * K, p=[0.2, 0.8]).reshape(K, K)

def update(data):
  global grid
  # copying grid
  # go line by line
  Ngrid = grid.copy()
  for i in range(K):
    for j in range(K):
      # sum of all neigbours
      # using boundary conditions

      total = (grid[i, (j-1) % K] + grid[i, (j + 1) % K] +
               grid[(i-1) % K, j] + grid[(i + 1) % K, j] +
               grid[(i-1) % K, (j - 1) % K] + grid[(i - 1) % K, (j + 1) % K] +
               grid[(i+1) % K, (j - 1) % K] + grid[(i + 1) % K, (j + 1) % K]) / 255
      # Conway's rules
      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          Ngrid[i, j] = OFF
      else:
        if total == 3:
          Ngrid[i, j] = ON

  mat.set_data(Ngrid)
  grid = Ngrid
  return [mat]

# animation setup
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()