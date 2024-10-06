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
import time


monkeys = []
monkeys_ernesti = []
monkeys_kernesti = []

# Peliluokka
class Game:
    def __init__(self):
        # Alusta Pygame
        pygame.init()

        # Aseta näyttö
        self.width, self.height = 800, 600  # Muuta tarpeen mukaan
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Apinat töissä')

        # Määrittele värit
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)  # Määrittele sininen väri

        # Pelin tila muuttujat
        global running
        self.running = [True]

        # Alusta objektit
        self.Saari = Island(600,500,(self.width/7,50))
        self.Allas = Pool(self.Saari.rect.centerx-100,self.Saari.rect.top+200)

        # Lasketaan matka 
        self.pool_northside_distance = self.Allas.rect.top - self.Saari.rect.top
        print("etäisyys",self.pool_northside_distance)
        # Ojat
        self.Oja_Ernesti = Ditch(self.Allas.rect.centerx-70,self.Saari.rect.top, self.pool_northside_distance, "Ernestin oja")
        self.Oja_Kernesti = Ditch(self.Allas.rect.centerx+60,self.Saari.rect.top, self.pool_northside_distance, "Kernestin Oja")

        self.Metsa = Forest(200,100,(self.Saari.rect.centerx-100,self.Saari.rect.centerx-10))

        # Napit
        self.Nappi_ernesti_kutsu = Button(self.black,10,450,20,"Ernesti hae apina töihin")

        self.Nappi_ernesti_kaiva = Button(self.black,10,500,20, "Kaiva ernestin apina")

        self.Nappi_kernesti_kutsu = Button(self.black,500,450,20,"Kernesti hae apina töihin")

        self.Nappi_kernesti_kaiva = Button(self.black,500,500,20, "Kaiva kernestin apina")

        self.Nappi_tayta_ojat = Button(self.black,self.width/3,550,20,"Täytä ojat")

        self.Nappi_kernesti10_apinaa = Button(self.black,10,550,20,"1+9 Apinaa töihin")

        self.create_monkeys()

    def create_monkeys(self):
        global monkeys
        global monkeys_ernesti
        global monkeys_kernesti
        
        monkey_start_x = self.Metsa.rect.left + 10  # Alkuasema x
        monkey_start_y = self.Metsa.rect.top + 10  # Alkuasema y
        monkey_spacing = 25  # Etäisyys apinoiden välillä

        for i in range(20):  # Luo 20 apinaa
            x = monkey_start_x + (i % 5) * monkey_spacing  # Järjestä 5 sarakkeeseen
            y = monkey_start_y + (i // 5) * monkey_spacing  # Järjestä riveihin

            # Vaihda puoli indeksin mukaan
            side = "Right" if i % 2 == 0 else "Left"

            monkey = Monkey(30, 30, (x, y), self.running, side=side)  # Luo apina-objekti
            monkeys.append(monkey)  # Lisää apinoiden listaan

    def process_input(self):
        # Tapahtumankäsittely
        global ernesti_apina_kaivuu_kahva
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running[0] = False

                # Tyhjennä nukkumiset, jotta ei jäädytä
                for monkey in monkeys_ernesti:
                    monkey.sleep_event.clear()

                for monkey in monkeys_kernesti:
                    monkey.sleep_event.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # saa hiiren sijainnin

                # tarkistaa, onko hiiren sijainti napin päällä
                if self.Nappi_ernesti_kutsu.button_rect.collidepoint(mouse_pos):
                    print("Ernesti Apina hommiin stna")
                    ## SIIRRÄ YKSI APINA Oja_Ernesti
                    if monkeys:
                        # Otetaan ensimmäinen apina
                        moving_monkey = monkeys.pop(0)  # Otetaan pois listasta ja siirretään ernestin listaan
                        monkeys_ernesti.append(moving_monkey)
                        threading.Thread(target= moving_monkey.move_to_last, args=(self.Oja_Ernesti,)).start()

                if self.Nappi_kernesti_kutsu.button_rect.collidepoint(mouse_pos):
                    print("Kernesti Apina hommiin stna")
                    ## SIIRRÄ YKSI APINA Oja_Ernesti
                    if monkeys:
                        # Otetaan ensimmäinen apina
                        moving_monkey = monkeys.pop(0)  # Otetaan pois listasta ja siirretään kernestin listaan
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
                    # Täytä molemmat matriisit ykkösillä
                    self.Oja_Ernesti.ditch_matrix.fill(1)  # Käytä fill asettaaksesi kaikki elementit ykkösiksi
                    self.Oja_Kernesti.ditch_matrix.fill(1)  # Käytä fill asettaaksesi kaikki elementit ykkösiksi

                if self.Nappi_kernesti10_apinaa.button_rect.collidepoint(mouse_pos):
                    self.digging_counter = 0
                    self.start_digging()

    def start_digging(self):
        if monkeys and self.digging_counter < 10:
            moving_monkey = monkeys.pop(0)  # Poista ensimmäinen apina listasta
            monkeys_kernesti.append(moving_monkey)
            threading.Thread(target=moving_monkey.random_dig, args=(self.Oja_Ernesti,)).start()
            # Aikatauluta seuraavan apinan kaivaminen viiveen jälkeen
            threading.Timer(1, self.start_digging).start()  # Kutsu metodia uudelleen 1 sekunnin kuluttua
            self.digging_counter += 1

    def update(self):
        # Päivitä pelilogiikka
        pass  # Lisää päivittämislokiikka tänne

    def render(self):
        # Täytä tausta sinisellä
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
        self.Nappi_kernesti10_apinaa.draw(self.screen)

        for monkey in monkeys:
            monkey.draw(self.screen) 

        for monkey in monkeys_ernesti:
            monkey.draw(self.screen)

        for monkey in monkeys_kernesti:
            monkey.draw(self.screen)

        # Päivitä näyttö
        pygame.display.flip()

    def run(self):
        # Pääpelisilmukka
        while self.running[0]==True:
            self.process_input()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()


# Käynnistä peli
if __name__ == "__main__":
    game = Game()
    game.run()
