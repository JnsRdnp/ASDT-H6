import pygame

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

    def draw(self, screen):
        # Create a white surface to draw on
        white_surface = pygame.Surface(self.rect.size)
        white_surface.fill((255, 255, 255))  # Fill the surface with white
        screen.blit(white_surface, self.rect)  # Draw the white surface first
        screen.blit(self.resized_image, self.rect)  # Then draw the monkey image on top
