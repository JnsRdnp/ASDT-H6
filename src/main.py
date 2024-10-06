import pygame
import sys
import threading
import numpy as np
from island import Island
from pool import Pool
from ditch import Ditch
from forest import Forest
from monkey import Monkey
from button import Button


monkeys = []
monkeys_ernesti = []
monkeys_kernesti = []

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
        global running
        self.running = [True]

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

        self.Nappi_ernesti_kaiva = Button(self.black,10,550,20, "Kaiva ernestin apina")

        self.Nappi_kernesti_kutsu = Button(self.black,500,500,20,"Kernesti hae apina töihin")

        self.Nappi_kernesti_kaiva = Button(self.black,500,550,20, "Kaiva kernestin apina")

        self.Nappi_tayta_ojat = Button(self.black,self.width/3,550,20,"Täytä ojat")

        self.create_monkeys()

    def create_monkeys(self):
        global monkeys
        global monkeys_ernesti
        global monkeys_kernesti
        
        monkey_start_x = self.Metsa.rect.left + 10  # Starting position x
        monkey_start_y = self.Metsa.rect.top + 10  # Starting position y
        monkey_spacing = 25 # Space between monkeys

        for i in range(20):  # Create 20 monkeys
            x = monkey_start_x + (i % 5) * monkey_spacing  # Arrange in 5 columns
            y = monkey_start_y + (i // 5) * monkey_spacing  # Arrange in rows

            # Alternate side based on the index
            side = "Right" if i % 2 == 0 else "Left"

            monkey = Monkey(30, 30, (x, y), self.running, side=side)  # Instantiate a Monkey object
            monkeys.append(monkey)  # Add to the list of monkeys




    def process_input(self):
        # Event handling
        global ernesti_apina_kaivuu_kahva
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running[0] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if self.Nappi_ernesti_kutsu.button_rect.collidepoint(mouse_pos):
                    print("Ernesti Apina hommiin stna")
                    ## MOVE ONE MONKEY TO Oja_Ernesti
                    if monkeys:
                        # Otetaan ensimmäinen apina
                        moving_monkey = monkeys.pop(0)  # Otetaan pois listasta ja siirretään ernestin listaan
                        monkeys_ernesti.append(moving_monkey)
                        threading.Thread(target= moving_monkey.move_to_last, args=(self.Oja_Ernesti,)).start()

                if self.Nappi_kernesti_kutsu.button_rect.collidepoint(mouse_pos):
                    print("Kernesti Apina hommiin stna")
                    ## MOVE ONE MONKEY TO Oja_Ernesti
                    if monkeys:
                        # Otetaan ensimmäinen apina
                        moving_monkey = monkeys.pop(0)  # Otetaan pois listasta ja siirretään ernestin listaan
                        monkeys_kernesti.append(moving_monkey)
                        threading.Thread(target= moving_monkey.move_to_last, args=(self.Oja_Kernesti,)).start()      

                if self.Nappi_ernesti_kaiva.button_rect.collidepoint(mouse_pos):
                    # ernesti_apina_kaivuu_kahva.start()
                    if monkeys_ernesti:
                        for monkey in monkeys_ernesti:
                            if monkey.apina_kaivaa == False and monkey.kaivuu_kahva != None:
                                monkey.kaivuu_kahva.start()

                if self.Nappi_kernesti_kaiva.button_rect.collidepoint(mouse_pos):
                    # ernesti_apina_kaivuu_kahva.start()
                    if monkeys_kernesti:
                        for monkey in monkeys_kernesti:
                            if monkey.apina_kaivaa == False and monkey.kaivuu_kahva != None:
                                monkey.kaivuu_kahva.start()

                if self.Nappi_tayta_ojat.button_rect.collidepoint(mouse_pos):
                    # Fill both matrices with ones
                    self.Oja_Ernesti.ditch_matrix.fill(1)  # Use fill to set all elements to 1
                    self.Oja_Kernesti.ditch_matrix.fill(1)  # Use fill to set all elements to 1



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
        self.Nappi_ernesti_kaiva.draw(self.screen)
        self.Nappi_kernesti_kutsu.draw(self.screen)
        self.Nappi_kernesti_kaiva.draw(self.screen)
        self.Nappi_tayta_ojat.draw(self.screen)


        for monkey in monkeys:
            monkey.draw(self.screen) 

        for monkey in monkeys_ernesti:
            monkey.draw(self.screen)

        for monkey in monkeys_kernesti:
            monkey.draw(self.screen)

        # Update the display
        pygame.display.flip()

    def run(self):
        # Main game loop
        while self.running[0]==True:
            self.process_input()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()


# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
