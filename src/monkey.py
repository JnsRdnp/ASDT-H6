import matplotlib.pyplot as plt
import numpy as np

class Monkey:
    def __init__(self, x, y):
        self.x = x  # Current x position
        self.y = y  # Current y position
        self.size = 2  # Size of the monkey (2x2)
        self.speed = 1  # Speed of movement per step

    def draw(self, ax):
        """Draw the monkey on the provided axes."""
        ax.add_patch(plt.Rectangle((self.x, self.y), self.size, self.size, color='brown'))

    def move(self, target_x, target_y):
        """Move the monkey incrementally towards a target position."""
        # Calculate the distance to the target
        dx = target_x - self.x
        dy = target_y - self.y
        distance = np.hypot(dx, dy)  # Calculate the distance

        if distance > 0:  # Ensure that the monkey has not reached the target
            # Normalize the direction vector
            dx /= distance
            dy /= distance

            # Move the monkey in the direction of the target, scaled by the speed
            self.x += dx * self.speed
            self.y += dy * self.speed