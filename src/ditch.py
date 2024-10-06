import pygame
import numpy as np

class Ditch(pygame.sprite.Sprite):
    def __init__(self,x,y, distance ,ppu=1):
        super().__init__()
        self.ppu = ppu  # Pixels per unit
        self.width_units = 3  # Width in units
        self.height_units = distance   # Height in units (20 units * 3 pixels/unit = 60 pixels)

        self.one_meter = distance/100
        
        # Create a 20x6 matrix for the pool
        self.pool_matrix = np.ones((self.height_units, self.width_units), dtype=int)
        print(self.pool_matrix)

        # Define pool color
        self.pool_color = (255, 255, 255) # Cyan
        
        # Position and size
        self.rect = pygame.Rect(x, y, self.width_units * self.ppu, self.height_units * self.ppu)

    def draw(self, screen):
        # Draw the pool based on the matrix
        for row in range(self.pool_matrix.shape[0]):
            for col in range(self.pool_matrix.shape[1]):
                if self.pool_matrix[row, col] == 1:  # Check if the matrix value is 1
                    pygame.draw.rect(screen, self.pool_color,
                                     (self.rect.x + col * self.ppu,
                                      self.rect.y + row * self.ppu,
                                      self.ppu, self.ppu))