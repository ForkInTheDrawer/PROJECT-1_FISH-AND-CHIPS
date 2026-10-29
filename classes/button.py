import pygame


class Button:
    def __init__ (self, text, text_color, rect, hover_color):

        self.text = text
        self.text_color = text_color
        self.rect = rect
        self.x, self.y = rect.x, rect.y
        self.width, self.height = rect.size
        self.hover_color = hover_color

        self.font = pygame.font.Font("None", 30)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()  #gets mouse pos
        
        #current_color = self.hover_color if self.hover_color.colliderect(mouse_pos) else self.color

        pass #NOTE: WORK ON BUTTONS
    