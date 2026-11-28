# Gear system from inventory system (done to make gear system clearer + easier to maintain)

import pygame

class GearWindow:
    def draw(self, screen, window_rect, 
             inventory, border_color, 
             info_font, text_color, 
             dragging_inventory_index = None,
             toolbar_slots = None,
             toolbar_slot_rects = None
             ):

        dragged_item = None

        if dragging_inventory_index is not None:
            items = inventory["plr_inv"]

            if 0 <= dragging_inventory_index < len(items):
                dragged_item = items[dragging_inventory_index]

        #Pulsing animation

        pulse_phase = (pygame.time.get_ticks() % 1200 / 1200)
        pulse_amount = 1 - abs(2 * pulse_phase - 1)


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
        slot_width = 68
        slot_height = 65
        slot_gap = 8

        slot_start_y = panel_rect.centery - (
            (4 * slot_height + 3 * slot_gap) // 2
        )
        equipment_slots = ["Head", "Body", "Ring", "Boots"]
        #Loop for slots
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
                border_radius= 7
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

        items_by_slot = self.get_visible_items_by_slot(inventory)



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
        mouse_pos = pygame.mouse.get_pos()
        hovered_toolbar_index = None

        if toolbar_slot_rects:
            for index, slot_rect in enumerate(toolbar_slot_rects):
                if slot_rect.collidepoint(mouse_pos):
                    hovered_toolbar_index = index
                    break
        #Grid
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
            #Grid drawing (again)
            if (
                slot_index in items_by_slot
                and items_by_slot[slot_index][0] != dragging_inventory_index
                ):
                _, item = items_by_slot[slot_index]

                item_name = str(item.get("name", "Unknown"))
                item_category = str(item.get("category", "Unknown"))
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

        # Gear item inspection

        selected_item = None

        if dragging_inventory_index is None:

            # First priority: item hovered in Gear grid
            if hovered_index is not None and hovered_index in items_by_slot:
                _, selected_item = items_by_slot[hovered_index]

            # Second priority: item hovered in toolbar slot 1
            elif (
                hovered_toolbar_index == 0
                and toolbar_slots is not None
                and len(toolbar_slots) > 0
            ):
                selected_item = toolbar_slots[0]

        if selected_item is not None:

            pygame.draw.rect(
                screen,
                (25, 62, 76),
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
                "GEAR DETAILS",
                True,
                text_color
            )

            screen.blit(
                panel_title,
                (panel_rect.x + 12, panel_rect.y + 15)
            )

            details_font = pygame.font.Font(None, 20)
            text_x = panel_rect.x + 12
            text_y = panel_rect.y + 55
            max_width = panel_rect.width - 24
            line_height = 23

            details = [
                ("Name: ", selected_item.get("name", "Unknown")),
                ("Category: ", selected_item.get("category", "Unknown")),
                ("Description: ", selected_item.get(
                    "description",
                    "No description available."
                ))
            ]

            stats = selected_item.get("stats", {})

            if stats:
                details.append(("Stats:", ""))

                for stat_name, stat_value in stats.items():
                    details.append((f"{stat_name}: ", stat_value))

            if "quantity" in selected_item:
                details.append(("Quantity: ", selected_item["quantity"]))

            # Wrap text
            wrapped_lines = []

            for label, value in details:
                prefix = label
                words = str(value).split()
                current_line = prefix
                continuation_indent = details_font.size(prefix)[0]
                current_indent = 0

                for word in words:
                    test_line = (
                        current_line + word
                        if current_line == prefix
                        else current_line + " " + word
                    )

                    if details_font.size(test_line)[0] <= max_width:
                        current_line = test_line
                    else:
                        wrapped_lines.append((current_line, current_indent))
                        current_line = word
                        current_indent = continuation_indent

                wrapped_lines.append((current_line, current_indent))

            # Draw details
            for index, (line, indent) in enumerate(wrapped_lines):
                if text_y + index * line_height > panel_rect.bottom - 20:
                    break

                detail_text = details_font.render(
                    line,
                    True,
                    text_color
                )

                screen.blit(
                    detail_text,
                    (text_x + indent, text_y + index * line_height)
                )


    def draw_floating_card(self, screen, inventory, dragging_inventory_index, text_color):
        if dragging_inventory_index is None:
            return
        items = inventory["plr_inv"]

        if not 0 <= dragging_inventory_index < len(items):
            return
        dragged_item = items[dragging_inventory_index]
        mouse_x, mouse_y = pygame.mouse.get_pos()

        card_rect = pygame.Rect(
            mouse_x + 12,
            mouse_y + 12,
            115,
            45
        )

        pygame.draw.rect(
            screen,
            (25,62,76),
            card_rect,
            border_radius = 7
        )

        pygame.draw.rect(
            screen,
            (255, 210, 90),
            card_rect,
            2,
            border_radius = 7
        )

        drag_font = pygame.font.Font(None, 21)
        item_name = str(dragged_item.get("name", "Unknown"))

        while item_name and drag_font.size(item_name)[0] > card_rect.width-12:
            item_name = item_name[:-1]

        if item_name != dragged_item.get("name", "Unknown"):
            item_name += "..."

        drag_text = drag_font.render(
            item_name,
            True,
            text_color
        )

        screen.blit(
            drag_text,
            drag_text.get_rect(
                center = card_rect.center
            )
        )

    def draw_drag_card(self, screen, dragged_item, text_color):
        if dragged_item is None:
            return

        mouse_x, mouse_y = pygame.mouse.get_pos()

        card_rect = pygame.Rect(
            mouse_x + 12,
            mouse_y + 12,
            115,
            45
        )

        pygame.draw.rect(
            screen, (25, 62, 76), card_rect, border_radius = 7
        )
        pygame.draw.rect(
            screen, (255,210, 90), card_rect, 2, border_radius= 7
        )

        drag_font = pygame.font.Font(None, 21)
        item_name = str(dragged_item.get("name", "Unknown")) 

        while item_name and drag_font.size(item_name)[0] > card_rect.width - 12:
            item_name = item_name[:-1]

        if item_name != dragged_item.get("name", "Unknown"):
            item_name += "..."

        drag_text = drag_font.render(item_name, True, text_color)

        screen.blit(
            drag_text,
            drag_text.get_rect(center= card_rect.center)
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
        slot_index = self.get_slot_index_at_pos(
            mouse_pos,
            window_rect
        )

        if slot_index is None:
            return None

        visible_items = self.get_visible_items_by_slot(inventory)
        if slot_index not in visible_items:
            return None

        return visible_items[slot_index][0]


    def get_visible_items_by_slot(self, inventory):
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

        visible_items = {}
        next_slot = 0

        for inv_index, item in enumerate(inventory["plr_inv"]):
            category = str(item.get("category", "")).upper()

            if category not in gear_categories | consumable_categories:
                continue

            gear_slot = item.get("gear_slot")

            if (
                not isinstance(gear_slot, int)
                or not 0 <= gear_slot < 20
                or gear_slot in visible_items
            ):
                while next_slot in visible_items:
                    next_slot += 1
                gear_slot = next_slot

            visible_items[gear_slot] = (inv_index, item)
            next_slot = max(next_slot, gear_slot + 1)
        return visible_items
