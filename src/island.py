import pygame

class Island(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("./assets/island.png")
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

    def draw(self,screen):
        screen.blit(self.resized_image, self.rect)
