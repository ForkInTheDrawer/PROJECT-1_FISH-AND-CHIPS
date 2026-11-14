import pygame
from classes.ui_handling.button import Button



class ShopWindow:
    def __init__(self):
        self.rect = pygame.Rect(200, 300, 800, 400)

        self.title_font = pygame.font.Font(None, 48)
        self.info_font = pygame.font.Font(None, 28)

        self.buttons = [
            {
                "button" : Button(
                    "Basic Rod Upgrade - $25",
                    (255,255,255),
                    pygame.Rect(280,440,270,75),
                    (49,132, 92),
                    (70,160,110)
                ),
                "name" : "Basic Rod Upgrade",
                "price" : 25

            },
            {
                "button" : Button(
                    "Basic Luck - $100",
                    (255,255,255),
                    pygame.Rect(650,440,270,75),
                    (49,132,92),
                    (70,160,110)
                ),
                "name" : "Basic Luck Potion",
                "price" : 100
            }
        ]
    def draw(self, screen):
        pygame.draw.rect(screen, (90, 118, 125), self.rect)
        pygame.draw.rect(screen, (125, 97, 90), self.rect, 4)

        title = self.title_font.render(
            "FISHING SHOP",
            True,
            (255,255,255)
        )

        screen.blit(
            title,
            title.get_rect(
                center = (self.rect.centerx, 355)
            )
            )

        info = self.info_font.render(
            "TEST PURCHASES",
            True,
            (230,230,230)
            )
        screen.blit(
            info,
            info.get_rect(center = (self.rect.centerx, 400))
        )

        for item in self.buttons:
            item["button"].draw(screen)

    def handle_event(self, event):
        for item in self.buttons:
            if item["button"].is_clicked(event):
                return item["name"], item["price"]
        return None
    