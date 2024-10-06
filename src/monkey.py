import pygame

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

        self.current_index = None
        self.font = pygame.font.SysFont(None, 24)  # Set up the font for rendering text

    def draw(self, screen):
        # Draw the monkey image
        screen.blit(self.resized_image, self.rect)

        # Create the text surface for the current index
        if self.current_index is not None:
            index_text = f"Index: {self.current_index}"
            text_surface = self.font.render(index_text, True, (255, 255, 255))  # White text color
            text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Position below the monkey
            screen.blit(text_surface, text_rect)

    def move(self, target_position, matrix_index):
        """Move the monkey to the target position."""
        self.rect.bottomleft = target_position
        print("Apina liikkui tähän: ", self.rect.topleft)
        self.current_index = matrix_index  # Save the matrix index
