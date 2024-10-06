import pygame
import sys
from island import Island
from pool import Pool
from ditch import Ditch
from forest import Forest
from monkey import Monkey
from button import Button

monkeys = []

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

        # Lasketaan matka 
        self.pool_northside_distance = self.Allas.rect.top - self.Saari.rect.top
        
        # Ojat
        self.Oja_Ernesti = Ditch(self.Allas.rect.centerx-70,self.Saari.rect.top, self.pool_northside_distance, "Ernestin oja")
        self.Oja_Kernesti = Ditch(self.Allas.rect.centerx+60,self.Saari.rect.top, self.pool_northside_distance, "Kernestin Oja")

        self.Metsa = Forest(200,100,(self.Saari.rect.centerx-100,self.Saari.rect.centerx-10))

        # Napit
        self.Nappi_ernesti_kutsu = Button(self.black,10,500,20,"Ernesti hae apina töihin")

        self.create_monkeys()

    def create_monkeys(self):
        global monkeys
        monkey_start_x = self.Metsa.rect.left + 10  # Starting position x
        monkey_start_y = self.Metsa.rect.top + 10  # Starting position y
        monkey_spacing = 25 # Space between monkeys

        for i in range(20):  # Create 20 monkeys
            x = monkey_start_x + (i % 5) * monkey_spacing  # Arrange in 5 columns
            y = monkey_start_y + (i // 5) * monkey_spacing  # Arrange in rows
            monkey = Monkey(30,30,(x, y))  # Instantiate a Monkey object
            monkeys.append(monkey)  # Add to the list of monkeys


    def process_input(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if self.Nappi_ernesti_kutsu.button_rect.collidepoint(mouse_pos):
                    print("Apina hommiin stna")

    def update(self):
        # Update game logic
        pass  # Add your update logic here

    def render(self):
        # Fill the background with blue
        self.screen.fill(self.blue)
        self.Saari.draw(self.screen)
        self.Allas.draw(self.screen)
        self.Oja_Ernesti.draw(self.screen)
        self.Oja_Kernesti.draw(self.screen)
        self.Metsa.draw(self.screen)
        self.Nappi_ernesti_kutsu.draw(self.screen)

        for monkey in monkeys:
            monkey.draw(self.screen)  # Ensure that the Monkey class has a draw method

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
