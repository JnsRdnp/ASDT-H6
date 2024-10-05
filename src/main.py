import pygame
import sys
import numpy as np  # Import NumPy

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 520
SCREEN_HEIGHT = 520
FPS = 60  # Frames per second

# Grid constants
WIDTH = 3
HEIGHT = 3
MARGIN = 1
GRID_SIZE = 130  # Define your grid size (this should reflect your grid dimensions)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)  # Brown color
POOL_COLOR = (0, 255, 255)  # Cyan color for the pool

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
        # Dictionary to hold area marking values
        self.area_markings = {
            'island': 1,
            'pool': 2
        }
        # Mark the island area and the pool in the grid
        self.mark_area(4, 127, 4, 127, self.area_markings['island'])  # Island
        self.mark_area(104, 124, 35, 95, self.area_markings['pool'])    # Pool

    def mark_area(self, row_start, row_end, col_start, col_end, mark_value):
        """Marks an area in the grid with the specified value."""
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                if row < GRID_SIZE and col < GRID_SIZE:
                    self.grid[row, col] = mark_value  # Mark the specified area

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
                    # Set that location to three
                    self.grid[row, column] = 3
                    print("Click ", pos, "Grid coordinates: ", row, column)

    def draw(self):
        # Fill the screen with black background
        screen.fill(BLACK)
        # Draw the grid
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                color = BLUE
                if self.grid[row, column] == self.area_markings['island']:
                    color = BROWN  # Color the island brown
                if self.grid[row, column] == 3:
                    color = BLACK
                elif self.grid[row, column] == self.area_markings['pool']:
                    color = POOL_COLOR  # Color the pool cyan
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
