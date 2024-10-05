import matplotlib.pyplot as plt
import numpy as np
from island import Island
from pool import Pool
from oja import Oja
import random
from monkey import Monkey


def draw_forest(ax, island_size):

    forest_radius = 40  # Define the radius of the forest
    forest_centerx = island_size / 2  # Center of the forest in the x-axis
    forest_centery = island_size / 5  # Place the forest near the bottom of the island
    
    # Draw a green circular patch for the forest
    forest_circle = plt.Circle((forest_centerx, forest_centery), forest_radius, color='green', alpha=0.6)
    ax.add_patch(forest_circle)
    ax.text(forest_centerx, forest_centery, 'Metsä', color='white', ha='center', va='center', fontsize=10)
    
    # Generate and draw monkeys in the forest
    monkeys = []
    for _ in range(20):
        # Randomly place monkeys within the forest boundaries
        angle = random.uniform(0, 2 * np.pi)
        r = random.uniform(0, forest_radius)
        monkey_x = forest_centerx + r * np.cos(angle) - 1  # Adjust position for the size of the monkey (2x2)
        monkey_y = forest_centery + r * np.sin(angle) - 1

        monkey = Monkey(monkey_x, monkey_y)
        monkeys.append(monkey)  # Store the monkey in the list
        monkey.draw(ax)


def main():
    # Create island and pool objects
    island_size = 250
    island = Island(island_size)

    # Pool definitions
    pool_width = 60
    pool_height = 20
    pool_startx = island_size / 3
    pool_starty = island_size - 100 - pool_height
    pool = Pool(pool_width, pool_height)

    # Create Oja objects for Ernesti and Kernesti with calculated extents
    oja_width = 1
    oja_height = 100
    oja_ernesti = Oja(oja_width, oja_height, pool_startx + 20, pool_starty + pool_height, "Ernestin oja")
    oja_kernesti = Oja(oja_width, oja_height, pool_startx + 40, pool_starty + pool_height, "Kernestin oja")

    # Create a figure with a blue background
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='blue')

    # Draw the island
    island.draw()

    # Set the extent for the pool to position it inside the island
    pool_extent = (pool_startx, pool_startx + pool_width, pool_starty, pool_starty + pool_height)

    # Draw the pool and Oja objects
    pool.draw(pool_extent)
    oja_ernesti.draw(ax)  # Pass current axes to draw
    oja_kernesti.draw(ax)

    # Draw the forest with monkeys
    draw_forest(ax, island_size)

    # Show the plot
    plt.show()  # This line is essential to display the plot


if __name__ == "__main__":
    main()
