import matplotlib.pyplot as plt

class Monkey:
    def __init__(self, x, y, size=2):
        self.x = x
        self.y = y
        self.size = size  # Monkeys are 2x2 dots

    def draw(self, ax):
        """Draw the monkey as a 2x2 square."""
        monkey_patch = plt.Rectangle((self.x, self.y), self.size, self.size, color='brown')
        ax.add_patch(monkey_patch)