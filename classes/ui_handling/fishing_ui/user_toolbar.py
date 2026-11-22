#Toolbar for the playerrrr

import pygame

from classes.animations import easing
from classes.animations.animation import Animation

class Toolbar:
    def __init__(self, slot_size = 68, slot_gap = 8):
        self.slot_size = slot_size
        self.slot_gap = slot_gap

        self.bg_color = (90, 118, 125)
        self.border_color = (180, 177, 201)
        self.text_color = (200, 200, 213)

        self.slot_rects = []

        self.selected_bg_color = (82,107,113)
        self.selected_border_color = (222,232,228)


        self.selected_slot = 0
        self.selection_animation = None
        self.selected_scale = 1.0

        self.font = pygame.font.Font(None, 22)
        self.item_font = pygame.font.Font(None, 18)

    def select_slot(self, index):
        if not 0 <= index < 5:
            return
        if index == self.selected_slot:
            return
        self.selected_slot = index
        self.selected_scale = 1.0

        self. selection_animation = Animation(
            start_val = 1.0,
            end_val = 1.13,
            duration = 0.18,
            easing_function= easing.ease_out_back
        )


    def draw(self, screen, dt = 0, toolbar_slots = None):
        self.slot_rects = []

        total_width = (
            5 * self.slot_size + 4 * self.slot_gap
        )

        start_x = (screen.get_width() - total_width) // 2
        start_y = screen.get_height() - self.slot_size - 16

        if self.selection_animation is not None:
            self.selected_scale = self.selection_animation.update(dt)
            if self.selection_animation.finished_status:
                self.selection_animation = None

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

            is_selected = index == self.selected_slot
            draw_rect = slot_rect.copy()

            if is_selected:
                draw_rect = draw_rect.inflate(
                    int(self.slot_size * (self.selected_scale -1)),
                    int(self.slot_size * (self.selected_scale -1))
                )
            item = toolbar_slots[index] if toolbar_slots else None\


            if is_selected:
                bg_color = self.selected_bg_color
                border_color = self.selected_border_color
            elif item is None:
                bg_color = (55, 72, 76)
                border_color = (85, 100, 104)
            else:
                bg_color = self.bg_color
                border_color = self.border_color
            
            pygame.draw.rect(
                screen,
                bg_color,
                draw_rect,
                border_radius=8
            )
            pygame.draw.rect(
                screen,
                border_color,
                draw_rect,
                3 if is_selected else 2,
                border_radius=8
            )

            key_text = self.font.render(
                str(index + 1),
                True,
                self.text_color
            )

            screen.blit(
                key_text,
                (draw_rect.x + 5, draw_rect.y + 4)
            )

            if index == 0 and item is not None:
                item_name = str(item.get("name", "item"))
                item_text = self.item_font.render(
                    item_name,
                    True,
                    self.text_color
                )
                screen.blit(
                    item_text,
                    item_text.get_rect(
                        center = draw_rect.center
                    )
                )

    def get_slot_index_at_pos(self, mouse_pos):
        for index, slot_text in enumerate(self.slot_rects):
            if slot_text.collidepoint(mouse_pos):
                return index

        return None
