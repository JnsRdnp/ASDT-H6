import pygame
import sys
from island import Island
from pool import Pool
from ditch import Ditch
from forest import Forest
from monkey import Monkey
from button import Button

monkeys = []
monkeys_ernesti = []

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
        self.Allas = Pool(self.Saari.rect.centerx-100,self.Saari.rect.top+200)

        # Lasketaan matka 
        self.pool_northside_distance = self.Allas.rect.top - self.Saari.rect.top
        print("distance",self.pool_northside_distance)
        # Ojat
        self.Oja_Ernesti = Ditch(self.Allas.rect.centerx-70,self.Saari.rect.top, self.pool_northside_distance, "Ernestin oja")
        self.Oja_Kernesti = Ditch(self.Allas.rect.centerx+60,self.Saari.rect.top, self.pool_northside_distance, "Kernestin Oja")

        self.Metsa = Forest(200,100,(self.Saari.rect.centerx-100,self.Saari.rect.centerx-10))

        # Napit
        self.Nappi_ernesti_kutsu = Button(self.black,10,500,20,"Ernesti hae apina töihin")

        self.create_monkeys()

    def create_monkeys(self):
        global monkeys
        global monkeys_ernesti
        monkey_start_x = self.Metsa.rect.left + 10  # Starting position x
        monkey_start_y = self.Metsa.rect.top + 10  # Starting position y
        monkey_spacing = 25 # Space between monkeys

        for i in range(20):  # Create 20 monkeys
            x = monkey_start_x + (i % 5) * monkey_spacing  # Arrange in 5 columns
            y = monkey_start_y + (i // 5) * monkey_spacing  # Arrange in rows
            monkey = Monkey(30,30,(x, y))  # Instantiate a Monkey object
            monkeys.append(monkey)  # Add to the list of monkeys

    def get_first_ditch_position(self, ditch):
        """Find the first available '1' in the ditch matrix and return its position."""
        for row in range(ditch.ditch_matrix.shape[0]):
            for col in range(ditch.ditch_matrix.shape[1]):
                if ditch.ditch_matrix[row, col] == 1:  # Find the first 1
                    # Calculate world coordinates of the matrix position
                    x = ditch.rect.x + col * ditch.ppu
                    y = ditch.rect.y + row * ditch.ppu
                    print("First ditch pos: ", x,y)
                    return (x, y)
        return None  # If no position is founds 
    
    def get_last_ditch_position(self, ditch):
        """Find the last available '1' in the ditch matrix and return its position and matrix index."""
        # Reverse iteration: Start from the last row and last column
        for row in range(ditch.ditch_matrix.shape[0] - 1, -1, -1):
            for col in range(ditch.ditch_matrix.shape[1] - 1, -1, -1):
                if ditch.ditch_matrix[row, col] == 1:  # Find the last 1
                    # Calculate world coordinates of the matrix position
                    x = ditch.rect.x + col * ditch.ppu
                    y = ditch.rect.y + row * ditch.ppu
                    print("Last ditch pos: ", x, y)
                    return (x, y), (row, col)  # Return both position and matrix index
        return None, None  # If no position is found


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
                    ## MOVE ONE MONKEY TO Oja_Ernesti
                    if monkeys:
                        # Get the first available monkey
                        moving_monkey = monkeys.pop(0)  # Remove it from the list
                        monkeys_ernesti.append(moving_monkey)
                        # Get the first (last in matrix) available position in the ditch
                        last_position, last_index = self.get_last_ditch_position(self.Oja_Ernesti)

                        if last_position and last_index:
                            moving_monkey.move(last_position, last_index)



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
            monkey.draw(self.screen) 

        for monkey in monkeys_ernesti:
            monkey.draw(self.screen)

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
