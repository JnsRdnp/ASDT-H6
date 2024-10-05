import matplotlib.pyplot as plt

class Monkey:
    def __init__(self, x, y):
        self.x = x  # Current x position
        self.y = y  # Current y position
        self.size = 2  # Size of the monkey (2x2)

    def draw(self, ax):
        """Draw the monkey on the provided axes."""
        ax.add_patch(plt.Rectangle((self.x, self.y), self.size, self.size, color='brown'))

    def move(self, target_x, target_y):
        """Move the monkey towards a target position."""
        # Here, you can implement your own logic for movement, such as moving one step at a time
        self.x = target_x
        self.y = target_y
