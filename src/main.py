import pygame
import sys
import numpy as np  # Import NumPy

# Grid basics on pygame http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60  # Frames per second

# Grid constants
WIDTH = 4
HEIGHT = 4
MARGIN = 1
GRID_SIZE = 120  # Define your grid size

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (211, 211, 211)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Grid Drawing Example')

# Set up the clock for FPS
clock = pygame.time.Clock()

class GridGame:
    def __init__(self):
        self.running = True
        # Create a 2-dimensional NumPy array (GRID_SIZE x GRID_SIZE)
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        # Initialize the grid with one cell set to one
        self.grid[1, 5] = 1

    def handle_events(self):
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Check if the click is within the grid boundaries
                if row < GRID_SIZE and column < GRID_SIZE:
                    # Set that location to one
                    self.grid[row, column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

    def draw(self):
        # Fill the screen with black background
        screen.fill(BLACK)
        # Draw the grid
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                color = WHITE
                if self.grid[row, column] == 1:
                    color = YELLOW
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Update the display
        pygame.display.flip()

    def run(self):
        # Main game loop
        while self.running:
            self.handle_events()
            self.draw()
            clock.tick(FPS)  # Control the frame rate

# Main entry point
if __name__ == "__main__":
    game = GridGame()
    game.run()

    # Clean up after the game loop ends
    pygame.quit()
    sys.exit()
