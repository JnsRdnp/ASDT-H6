import matplotlib.pyplot as plt
import numpy as np

class Oja:
    def __init__(self, width, height, startx, starty, name):
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty
        self.name = name  # Store the Oja's name
        self.grid = np.ones((self.height, self.width))  # Use a matrix to represent the ditch
        self.extent = self.calculate_extent()  # Calculate extent during initialization

    def calculate_extent(self):
        """Calculate and return the extent of the Oja based on its position and dimensions."""
        return (self.startx, self.startx + self.width, self.starty, self.starty + self.height)

    def draw(self, ax):
        """Draw the Oja using its matrix and display its name."""
        # Draw the Oja using imshow to represent the matrix
        ax.imshow(self.grid, extent=self.extent, aspect='auto', alpha=0.5)
        
        # Calculate the center position for the text
        center_x = (self.extent[0] + self.extent[1]) / 2
        center_y = (self.extent[2] + self.extent[3]) / 2

        # Add the Oja's name at the center of the ditch
        ax.text(center_x, center_y+55, self.name, color='black', ha='center', va='center', fontsize=4)
