import pygame
import sys
from island import Island
from pool import Pool
from ditch import Ditch



# Game class
class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.width, self.height = 800, 600  # Change as needed
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Monkeys at work')

        # Define colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)  # Define blue color

        # Game state variables
        self.running = True

        # Init objects
        self.Saari = Island(600,500,(self.width/7,50))
        self.Allas = Pool(self.Saari.rect.centerx-100,self.Saari.rect.centery)
        self.pool_northside_distance = self.Allas.rect.top - self.Saari.rect.top
        
        self.Oja_Ernesti = Ditch(self.Allas.rect.centerx-70,self.Saari.rect.top, self.pool_northside_distance)
        print(self.pool_northside_distance)


    def process_input(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Update game logic
        pass  # Add your update logic here

    def render(self):
        # Fill the background with blue
        self.screen.fill(self.blue)
        self.Saari.draw(self.screen)
        self.Allas.draw(self.screen)
        self.Oja_Ernesti.draw(self.screen)

        # Draw game objects here
        # Example: pygame.draw.rect(self.screen, self.black, (50, 50, 100, 100))

        # Update the display
        pygame.display.flip()

    def run(self):
        # Main game loop
        while self.running:
            self.process_input()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()


# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
