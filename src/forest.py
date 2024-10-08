import pygame

class Forest(pygame.sprite.Sprite):

    def __init__(self, width, height, location, monkeys=[]):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("./assets/forest.png")
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

    def draw(self,screen):
        screen.blit(self.resized_image, self.rect)
