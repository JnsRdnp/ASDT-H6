import pygame

# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame

class Button():

    pygame.font.init()

    def __init__(self, color, x,y, fontsize, text=''):
        self.color = color
        self.x = x
        self.y = y

        self.text = text


        self.my_font = pygame.font.SysFont('Comic Sans MS', fontsize)

        self.text_surface = self.my_font.render(self.text, False, (255, 255, 255))

        # Tekstin koko https://stackoverflow.com/questions/45384910/attributeerror-pygame-surface-object-has-no-attribute-rect
        text_rect = self.text_surface.get_rect()
        
        self.button_rect = pygame.Rect(self.x,self.y,text_rect.width+10,text_rect.height+2)
        

    def draw(self,screen):

        pygame.draw.rect(screen, self.color, self.button_rect, border_radius=5)
        screen.blit(self.text_surface, (self.button_rect.left+5, self.button_rect.top))

    def onClick(self):
        print("Nappia painettiin")
