import matplotlib.pyplot as plt
import numpy as np

class Pool:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.empty((self.height, self.width))
        self.grid.fill(0)  # Fill the empty array with zeros
        print(self.grid)

    def draw(self, extent):
        """Draws the pool on the plot."""
        plt.imshow(self.grid, extent=extent, aspect='auto', alpha=0.5)