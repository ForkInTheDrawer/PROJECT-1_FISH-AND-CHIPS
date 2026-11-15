import pygame

from classes.ui_handling.button import Button

class SellMenu:
    def __init__(self):
        self.width = 760
        self.height = 500

        self.bg_color = (16,43,58)
        self.border_color = (115,226,208)
        self.text_color = (244, 231, 197)

        self.title_font = pygame.font.Font(None, 48)

        self.rect = pygame.Rect(
            0,0,
            self.width,
            self.height
        )

        self.buttons = {
            "everything" : Button(
                "Everything",
                (255,255,255),
                pygame.Rect(0,0,620,60),
                (49,132, 92),
                (70,160,110)
            ),
            "manual" : Button(
                "I want to sell something in my inventory.",
                (255,255,255),
                pygame.Rect(0,0, 620, 60),
                (49, 132, 92),
                (70, 160, 110)
            ),

            "worth" : Button(
                "How much is my inventory worth?",
                (255,255,255),
                pygame.Rect( 0,0, 620, 60),
                (49, 132, 92),
                (70, 160, 110)
            ),
            "cancel" : Button(
                "Nevermind.",
                (255,255,255),
                pygame.Rect( 0, 0 , 620, 60),
                (169, 67,67),
                (200,85,85)
            )
        }

    def draw(self,screen):

        #Overlay:
        overlay = pygame.Surface(
            screen.get_size(),
            pygame.SRCALPHA
        )
        overlay.fill((0,0,0,150))
        screen.blit(overlay, (0,0))


        #Menu (Centered)
        self.rect.center = screen.get_rect().center
        pygame.draw.rect(
            screen,
            self.bg_color,
            self.rect,
            border_radius= 10
        )
        pygame.draw.rect(
            screen,
            self.border_color,
            self.rect,
            3,
            border_radius= 10
        )
        title = self.title_font.render(
            "What would You Like to sell?",
            True,
            self.text_color
        )
        screen.blit(
            title,
            title.get_rect(
                center = (self.rect.centerx, self.rect.y + 75)
            )
        )

        #Positions:
        button_y = self.rect.y + 140

        for button in self.buttons.values():
            button.rect.centerx = self.rect.centerx
            button.rect.y = button_y

            button.draw(screen)

            button_y += 80
            
    def handle_event(self, event):
        for choice, button in self.buttons.items():
            if button.is_clicked(event):
                return choice
        return None