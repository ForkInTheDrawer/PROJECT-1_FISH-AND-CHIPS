import pygame


class Button:
    def __init__ (self, text, text_color, rect, color,  hover_color):

        self.text = text
        self.text_color = text_color
        self.rect = rect
        self.x, self.y = rect.x, rect.y
        self.width, self.height = rect.size
        self.color = color
        self.hover_color = hover_color

        self.font = pygame.font.Font(None, 30)



    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        current_color = ( self.hover_color if self.rect.collidepoint(mouse_pos) else self.color)

        pygame.draw.rect(surface, current_color, self.rect) #draws bg


        text_surface = self.font.render(self.text, True, self.text_color)

        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

        return False
        