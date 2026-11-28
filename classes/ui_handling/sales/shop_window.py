# Shopping stuffs

import pygame
from classes.ui_handling.button import Button



class ShopWindow:
    def __init__(self, stock = None):

        self.rect = pygame.Rect(200,300,800,400)
        self.stock = stock or []

        self.title_font = pygame.font.Font(None, 48)
        self.info_font = pygame.font.Font(None, 25)
        self.item_font = pygame.font.Font(None, 23)
        self.small_font = pygame.font.Font(None, 19)

        self.item_rects = []

        for index in range(len(self.stock)):
            column = index % 3
            row = index //3

            item_rect = pygame.Rect(
                220 + column * 250,
                430 + row * 115,
                230,
                105
            )

            self.item_rects.append(item_rect)

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
            title.get_rect(center = (self.rect.centerx, self.rect.y +55))
        )

        info = self.info_font.render(
            "AVAILABLE ITEMS",
            True,
            (230, 230, 230)
        )

        screen.blit(
            info,
            info.get_rect(center = (self.rect.centerx, 400))
        )

        for item, item_rect in zip(self.stock, self.item_rects):
            pygame.draw.rect(screen, (49, 80, 85), item_rect)
            pygame.draw.rect(screen, (180, 180, 180), item_rect, 2)

            name = self.item_font.render(
                item["name"], True, (255,255,255)
            )

            rarity = self.small_font.render(
                item["rarity"], True, (230, 220, 150)
            )

            price = self.small_font.render(
                f'${item["price"]}', True, (120, 255, 150)
            )

            screen.blit(name, (item_rect.x + 8, item_rect.y + 8))
            screen.blit(rarity, (item_rect.x + 8, item_rect.y + 8))
            screen.blit(price, (item_rect.x + 8, item_rect.y + 58))

            stats_text = ", ". join (
                f"{stat} : {value}"
                for stat, value in item["stats"].items()
            )

            stats = self.small_font.render(
            stats_text, 
            True,
            (220,220,220)
            )

            screen.blit(stats, (item_rect.x + 8, item_rect.y + 80))

    def handle_event(self, event):
        return None

    