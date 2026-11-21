import pygame

class Toolbar:
    def __init__(self, slot_size = 68, slot_gap = 8):
        self.slot_size = slot_size
        self.slot_gap = slot_gap

        self.bg_color = (90, 118, 125)
        self.border_color = (180, 177, 201)
        self.text_color = (255, 255, 255)

        self.slot_rects = []


    def draw(self, screen):
        self.slot_rects = []

        total_width = (
            5 * self.slot_size + 4 * self.slot_gap
        )

        start_x = (screen.get_width() - total_width) // 2
        start_y = screen.get_height() - self.slot_size - 16

        for index in range(5):

            slot_rect = pygame.Rect(
                start_x + index * (
                    self.slot_size + self.slot_gap
                ),
                start_y,
                self.slot_size,
                self.slot_size
            )
            self.slot_rects.append(slot_rect)

            pygame.draw.rect(
                screen,
                self.bg_color,
                slot_rect,
                border_radius=8
            )
            pygame.draw.rect(
                screen,
                self.border_color,
                slot_rect,
                2,
                border_radius=8
            )

            key_text = pygame.font.Font(None, 22).render(
                str(index +1),
                True,
                self.text_color
            )

            screen.blit(
                key_text,
                (slot_rect.x + 5, slot_rect.y + 4)
            )

            if index == 0 :
                rod_text = pygame.font.Font(None, 23).render(
                    "ROD",
                    True,
                    self.text_color
                )

                screen.blit(
                    rod_text,
                    rod_text.get_rect(center = slot_rect.center)
                )