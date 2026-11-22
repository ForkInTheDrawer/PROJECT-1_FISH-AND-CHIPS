# Gear system from inventory system (done to make gear system clearer + easier to maintain)

import pygame

class GearWindow:
    def draw(self, screen, window_rect, inventory, border_color, info_font, text_color):
        panel_rect = pygame.Rect(
            window_rect.x + 25,
            window_rect.y + 120,
            240,
            350
        )

        pygame.draw.rect(
            screen,
            (25,62,76),
            panel_rect,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            border_color,
            panel_rect,
            2,
            border_radius=10
        )

        panel_title = info_font.render(
            "EQUIPMENT",
            True,
            text_color
        )

        screen.blit(
            panel_title,
            (panel_rect.x + 12, panel_rect.y + 12)
        )

        #char placeholder

        char_rect = pygame.Rect(
            panel_rect.x + 135,
            panel_rect.y + 130,
            80,
            80
        )

        pygame.draw.rect(
            screen,
            (210, 55,55),
            char_rect,
            border_radius = 5
        )

        #equipment slots

        equipment_slots = ["Head", "Body", "Ring", "Boots"]

        slot_width = 68
        slot_height = 65
        slot_gap = 8

        slot_start_y = panel_rect.centery - (
            (4 * slot_height + 3 * slot_gap) // 2
        )

        for index, slot_name in enumerate(equipment_slots):
            slot_rect = pygame.Rect(
                panel_rect.x + 20,
                slot_start_y + index * (
                    slot_height + slot_gap
                ),
                slot_width,
                slot_height
            )

            pygame.draw.rect(
                screen,
                (16,43,58),
                slot_rect,
                2,
                border_radius=7
            )

            slot_text = pygame.font.Font(None, 22).render(
                slot_name,
                True,
                text_color
            )

            screen.blit(
                slot_text,
                slot_text.get_rect(
                    center = (
                        slot_rect.centerx,
                        slot_rect.centery - 7
                    )
                )
            )
            empty_text = pygame.font.Font(None, 18).render(
                "Empty",
                True,
                (170,190,190)
            )

            screen.blit(
                empty_text,
                empty_text.get_rect(
                    center = (
                        slot_rect.centerx,
                        slot_rect.centery + 13
                    )
                )
            )
        # grid + filter
        gear_categories = {
            "HEAD",
            "BODY",
            "RING",
            "BOOTS",
            "GEAR",
            "FISHING ROD"
        }
        consumable_categories = {
            "CONSUMABLE",
            "CONSUMABLES"
        }

        items = [
            item for item in inventory["plr_inv"]
            if str(item.get("category", "")).upper()
            in gear_categories | consumable_categories
        ]



        slot_width = 76
        slot_height = 76
        slot_gap = 8
        columns = 5
        rows = 4

        grid_x = window_rect.x + 300
        grid_y = window_rect.y + 90
        hovered_index = self.get_slot_index_at_pos(
            pygame.mouse.get_pos(),
            window_rect
        )

        for slot_index in range(columns * rows):

            column = slot_index % columns
            row = slot_index // columns

            slot_rect = pygame.Rect(
                grid_x + column * (slot_width + slot_gap),
                grid_y + row * (slot_height + slot_gap),
                slot_width,
                slot_height
            )

            pygame.draw.rect(
                screen,
                (25,62,76),
                slot_rect,
                border_radius= 5
            )
            if slot_index == hovered_index:
                pygame.draw.rect(
                    screen,
                    (255, 210, 90),
                    slot_rect,
                    4,
                    border_radius= 5
                )
            else:
                pygame.draw.rect(
                    screen,
                    border_color,
                    slot_rect,
                    2,
                    border_radius= 5
                )

            if slot_index < len(items):
                item = items[slot_index]

                item_name = str(item.get("name", "Unknown"))
                item_category = str(
                    item.get("category", "Unknown")
                )

                name_font = pygame.font.Font(None, 19)

                detail_font = pygame.font.Font(None, 17)

                def fit_text(text, font, max_width):
                    text = str(text)

                    while text and font.size(text + "...")[0] > max_width:
                        text = text[:-1]
                    if text != str(item_name) and font.size(text + "...")[0] <= max_width:
                        text += "..."
                    return font.render(text, True, text_color)
                name_text = fit_text(item_name, name_font, slot_width - 10)
                category_text = fit_text(item_category, detail_font, slot_width - 10)

                screen.blit(
                    name_text,
                    name_text.get_rect(
                        center = (
                            slot_rect.centerx,
                            slot_rect.y + 25
                        )
                    )
                )

                screen.blit(
                    category_text,
                    category_text.get_rect(
                        center = (
                            slot_rect.centerx,
                            slot_rect.y + 50
                        )
                    )
                )

    def get_slot_index_at_pos(self, mouse_pos, window_rect):
        slot_width = 76
        slot_height = 76
        slot_gap = 8
        columns = 5
        rows = 4

        grid_x = window_rect.x + 300
        grid_y = window_rect.y + 90

        for slot_index in range(columns * rows):
            column = slot_index % columns
            row = slot_index // columns

            slot_rect = pygame.Rect(
                grid_x + column * (slot_width + slot_gap),
                grid_y + row * (slot_height + slot_gap),
                slot_width,
                slot_height
            )

            if slot_rect.collidepoint(mouse_pos):
                return slot_index

        return None

    def get_inv_index_at_pos(self, mouse_pos, window_rect, inventory):
        gear_categories = {
            "HEAD",
            "BODY",
            "RING",
            "BOOTS",
            "GEAR",
            "FISHING ROD"
        }

        consumable_categories = {
            "CONSUMABLE",
            "CATEGORIES"
        }

        visible_indexes = [
            index for index, item in enumerate(inventory["plr_inv"])
            if str(item.get("category", "")).upper()
            in gear_categories | consumable_categories
        ]


        slot_index = self.get_slot_index_at_pos(mouse_pos, window_rect)

        if slot_index is None or slot_index >= len(visible_indexes):
            return None

        return visible_indexes[slot_index]