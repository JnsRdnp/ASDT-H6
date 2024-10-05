import matplotlib.pyplot as plt
import numpy as np

class Oja:
    def __init__(self, width, height, startx, starty):
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty
        self.extent = self.calculate_extent()

    def calculate_extent(self):
        """Calculate and return the extent of the Oja based on its position and dimensions."""
        return (self.startx, self.startx + self.width, self.starty, self.starty + self.height)

    def draw(self, ax):
        """Draw the Oja on the given axes."""
        ax.add_patch(plt.Rectangle((self.startx, self.starty), self.width, self.height, color='orange'))
