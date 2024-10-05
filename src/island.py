import matplotlib.pyplot as plt
import numpy as np

class Island:
    def __init__(self, size):
        self.size = size
        self.color = [255, 255, 0]  # Yellow
        self.grid = np.zeros((self.size, self.size, 3), dtype=int)
        self.grid[:, :] = self.color  # Fill the island with yellow

    def draw(self):
        """Draws the island on the plot."""
        plt.imshow(self.grid, extent=(0, self.size, 0, self.size))
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        plt.axis('off')
