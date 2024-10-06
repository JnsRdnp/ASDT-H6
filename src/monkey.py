import pygame

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location
        

    def draw(self, screen):
        screen.blit(self.resized_image, self.rect)

    def move(self, target_position):
        """Move the monkey to the target position."""
        self.rect.topleft = target_position
        print("APina liikkui tähän: ",self.rect.topleft)

    def dig(self, matrix):
        pass