import pygame
import time
import threading

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

        self.current_index = None
        self.font = pygame.font.SysFont(None, 24)  # Set up the font for rendering text

        self.kaivuu_kahva = None

    def draw(self, screen):
        # Draw the monkey image
        screen.blit(self.resized_image, self.rect)

        # Create the text surface for the current index
        if self.current_index is not None:
            index_text = f"Index: {self.current_index}"
            text_surface = self.font.render(index_text, True, (255, 255, 255))  # White text color
            text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Position below the monkey
            screen.blit(text_surface, text_rect)

    def dig(self):
        for i in range(10):
            print("Apina kaivaa...")
            time.sleep(0.5)


    def move_to_last(self, Ditch):
        """Move the monkey to the target position."""
        self.target_location, self.current_index=self.get_last_ditch_position(Ditch)
        
        self.rect.bottomleft = self.target_location
        print("Apina liikkui tähän: ", self.rect.topleft)

        self.kaivuu_kahva = threading.Thread(target=self.dig)

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
