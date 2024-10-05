import matplotlib.pyplot as plt
import numpy as np
from island import Island
from pool import Pool


def main():
    # Create island and pool objects
    island_size = 250
    island = Island(island_size)
    
    pool_width = 60
    pool_height = 20
    pool = Pool(pool_width, pool_height)

    # Create a figure with a blue background
    plt.figure(figsize=(6, 6), facecolor='blue')

    # Draw the island
    island.draw()

    # Set the extent for the pool to position it inside the island
    pool_extent = (115, 175, 90, 110)  # Position the pool inside the island

    # Draw the pool
    pool.draw(pool_extent)

    # Show the plot
    plt.show()  # This line is essential to display the plot

if __name__ == "__main__":
    main()
