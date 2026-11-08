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



class DropdownMenu:
    def __init__(
            self, 
            options, 
            rect, 
            font = None, 
            bg_color = (35,55,65),
            hover_color = (55,85,95), 
            text_color = (255,255,255), 
            border_color = (115,226, 208)
    ):

        self.options = options
        self.rect = rect
        self.font = font or pygame.font.Font(None, 26)

        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_color = border_color

        self.is_open = False
        self.selected_option = None
        self.row_height = 34
        self.option_rects = []

    def get_option_rects(self):
        self.option_rects = []

        for index in range( len( self.options)):
            option_rect = pygame.Rect(
                self.rect.x,
                self.rect.bottom + index * self.row_height,
                self.rect.width,
                self.row_height
            )
            self.option_rects.append(option_rect)
        return self.option_rects

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        #Dropdown button:

        current_color = (
            self.hover_color
            if self.rect.collidepoint(mouse_pos)
            else self.bg_color
        )
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(
            surface, self.border_color, self.rect, 2
        )

        label = self.selected_option or "Sort By"

        text_surface = self.font.render(
            label, True, self.text_color
        )
        surface.blit(
            text_surface,
            text_surface.get_rect(
                mid_left = (self.rect.x + 10, self.rect.centery)
            )
        )

        #Dropdown Arrow

        arrow_x = self.rect.right - 16
        arrow_y = self.rect.centery

        pygame.draw.polygon(
            surface, 
            self.text_color,
            [
                (arrow_x - 5, arrow_y - 3),
                (arrow_x + 5, arrow_y -3),
                (arrow_x, arrow_y +4)

            ]
        )

        #OPTIONS:

        if self.is_open:
            for index, option_rect in enumerate( self.get_option_rects()):
                color = (
                    self.hover_color
                    if option_rect.collidepoint(mouse_pos)
                    else self.bg_color
                )

                pygame.draw.rect(
                    surface, color, option_rect
                )
                pygame.draw.rect(
                    surface, self.border_color, option_rect, 1
                )

                option_text = self.font.render(
                    str(self.options[index]),
                    True,
                    self.text_color
                )

                surface.blit(
                    option_text,
                    option_text.get_rect(
                        mid_left = (
                            option_rect.x + 10,
                            option_rect.centery
                        )
                    )
                )
        def handle_event(self, event):
            pass # NOTE: WORK ON THIS TOMORROW
        