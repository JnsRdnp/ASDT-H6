import pygame
import numpy as np

class Ditch(pygame.sprite.Sprite):
    def __init__(self, x, y, distance, name, ppu=1):
        super().__init__()
        self.ppu = ppu  # Pixels per unit
        self.width_units = 3  # Width in units
        self.height_units = distance  # Height in units
        self.name = name

        # Create a 20x6 matrix for the ditch
        self.pool_matrix = np.ones((self.height_units, self.width_units), dtype=int)
        print(self.pool_matrix)

        # Define ditch color
        self.pool_color = (255, 255, 255)  # White

        # Position and size
        self.rect = pygame.Rect(x, y, self.width_units * self.ppu, self.height_units * self.ppu)

        # Initialize font for text rendering
        self.font = pygame.font.Font(None, 24)  # Use default font and size 24

    def draw(self, screen):
        # Draw the ditch based on the matrix
        for row in range(self.pool_matrix.shape[0]):
            for col in range(self.pool_matrix.shape[1]):
                if self.pool_matrix[row, col] == 1:  # Check if the matrix value is 1
                    pygame.draw.rect(screen, self.pool_color,
                                     (self.rect.x + col * self.ppu,
                                      self.rect.y + row * self.ppu,
                                      self.ppu, self.ppu))
        
        # Render the name text
        text_surface = self.font.render(self.name, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.y - 15))  # Centered above the ditch
        screen.blit(text_surface, text_rect)  # Draw the text on the screen
