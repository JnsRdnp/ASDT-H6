import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60  # Frames per second

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Your Game Title')

# Set up the clock for FPS
clock = pygame.time.Clock()

# Colors (optional)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main Game Class (Optional)
class Game:
    def __init__(self):
        self.running = True

    def handle_events(self):
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Game logic updates go here
        pass

    def draw(self):
        # Drawing everything on the screen
        screen.fill(WHITE)  # Fill screen with white background
        # Add your game objects' drawing code here
        pygame.display.flip()  # Update the display

    def run(self):
        # Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(FPS)  # Control the frame rate

# Main entry point
if __name__ == "__main__":
    game = Game()
    game.run()

    # Clean up after the game loop ends
    pygame.quit()
    sys.exit()
