import pygame

from classes.ui_handling.button import DropdownMenu


class InventoryWindow:
    def __init__(self, size = (760, 560)):
        self.width, self.height = size

        self.background_color = (16,43,58)
        self.border_color = (255, 255, 255)
        self.text_color = (244,231,197)

        self.title_font = pygame.font.Font(None, 48)
        self.info_font = pygame.font.Font(None, 26)

        self.sort_dropdown = DropdownMenu(
            options = ["Default", "Category", "A-Z", "Rarity", "Weight"],
            rect = pygame.Rect(0, 0 ,140, 36)
        )

        self.sort_dropdown.selected_option = "Default"

        self.active_tab = "Items"
        self.tab_font = pygame.font.Font(None, 32)
        self.tabs = {
            "Items" : pygame.Rect(220,75,120,40),
            "Gear" : pygame.Rect(345, 75, 120, 40)
        }

    def wrap_text(self, text, font, max_width):
        words = str(text).split()
        lines = []
        current_line = ""

        for word in words:
            test_line = (
                word if not current_line
                else current_line + " " + word
            )

            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)

                if font.size(word)[0] > max_width:
                    chunk = ""
                    for char in word:
                        if font.size(chunk + char)[0] <= max_width:
                            chunk+= char
                        else:
                            if chunk:
                                lines.append(chunk)
                            chunk = char
                    current_line = chunk
                else:
                    current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 :
            for tab_name, tab_rect in self.tabs.items():
                if tab_rect.collidepoint(event.pos):
                    self.active_tab = tab_name
                    return tab_name
        return None

    def draw(self,screen , inventory, hovered_index = None, is_dragging = None):
        overlay = pygame.Surface(screen.get_size() , pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        screen.blit(overlay, (0,0))

        window_rect = pygame.Rect(
            0,0,
            self.width, self.height
        )
        window_rect.center = screen.get_rect().center



        pygame.draw.rect(
            screen, self.background_color, window_rect, border_radius = 10
        )
        pygame.draw.rect(
            screen, self.border_color, window_rect, 3, border_radius = 10
        )
        #Window Title
        title = self.title_font.render("INVENTORY", True, self.text_color)
        screen.blit(title, (window_rect.x + 25, window_rect.y + 20))

        #Tabs:
        for tab_name, tab_rect in self.tabs.items():

            tab_rect.topleft = (
                window_rect.x + (300 if tab_name == "Items" else 430),
                window_rect.y + 30
            )

            color = (
                (70,120,130)
                if self.active_tab == tab_name
                else(25,62,76)
            )

            pygame.draw.rect(screen,color,tab_rect, border_radius = 10)
            pygame.draw.rect(screen,self.background_color, tab_rect, 2, border_radius = 10)

            tab_text = self.tab_font.render(
                tab_name, True, self.text_color
            )

            screen.blit(
                tab_text,
                tab_text.get_rect(center = tab_rect.center)
            )

        if self.active_tab == "Items":


            #Item inspection Tab:

            panel_rect = pygame.Rect(
                window_rect.x + 25,
                window_rect.y + 120,
                240,
                350
            )
            pygame.draw.rect(screen, (25,62,76), panel_rect, border_radius = 10)
            pygame.draw.rect(screen, self.border_color, panel_rect, 2, border_radius = 10)

            panel_title = self.info_font.render(
                "ITEM DETAILS",
                True,
                self.text_color
            )
            screen.blit( panel_title, (panel_rect.x + 12, panel_rect.y + 15))

            items = inventory["plr_inv"]

            if hovered_index is not None and hovered_index < len(items):
                selected_item = items[hovered_index]
                details = [
                    f"Name: {selected_item.get('name', 'Unknown')}",
                    f"Category: {selected_item.get('category', 'Unknown')}",
                    f"Rarity: {selected_item.get('rarity', 'Common')}",
                    f"Mutation: {selected_item.get('mutation', 'None')}",
                    f"Weight: {selected_item.get('weight', 'N/A')}",
                    f"Locked: {'Yes' if selected_item.get('locked' ,False) else 'No'}",
                ]

                for color_key in ("COLOR_1", "COLOR_2"):
                    if color_key in selected_item:
                        details.append(f"Color {color_key[-1]}: {selected_item[color_key]}")

                if "price" in selected_item:
                    details.append(f"Price {selected_item['price']}")
                if "base_price" in selected_item:
                    details.append(F"Base Price: {selected_item['base_price']}")
                
                
                # Wrap inspection details:
                detail_font = pygame.font.Font(None,20)

                text_x = panel_rect.x + 12
                text_y = panel_rect.y + 60

                max_width = panel_rect.width - 24
                line_height = 24

                max_lines = (
                    panel_rect.bottom - 12 - text_y
                ) // line_height
                wrapped_details = []
                for detail in details:
                    wrapped_details.extend(
                        self.wrap_text( detail, detail_font, max_width)
                    )

                #prevents overflow

                if len(wrapped_details) > max_lines:
                    wrapped_details = wrapped_details[:max_lines]

                    last_line = wrapped_details [-1]

                    while last_line and detail_font.size(last_line + "...")[0] > max_width:
                        last_line = last_line[:-1]

                    wrapped_details[-1] = last_line + "..."
                #Draws textssssasdaddwasd:

                for index, line in enumerate(wrapped_details):
                    detail_text = detail_font.render(
                        line, True,
                        self.text_color
                    )

                    screen.blit(
                        detail_text,
                        (text_x, text_y + index * line_height)
                    )

            else:
                inspect_hint = pygame.font.Font(None, 24).render(
                    "Select an item to inspect.",
                    True,
                    self.text_color
                )
                screen.blit(
                    inspect_hint,
                    inspect_hint.get_rect(center = panel_rect.center)
                )




            #slot count
            item_count = len(inventory["plr_inv"])
            maximum_slots = inventory["maximum_slots"]

            slot_text = self.info_font.render(
                f"Slots: {item_count} / {maximum_slots}",
                True,
                self.text_color
            )

            screen.blit(
                slot_text,
                (window_rect.x + 28, window_rect.y + 80)
            )

            #TEMPORARY Placeholder:

            items = inventory["plr_inv"]

            slot_width = 80
            slot_height = 80
            slot_gap = 8
            columns = 5
            rows = 4

            grid_x = window_rect.x + 300
            grid_y = window_rect.y + 90

            hovered_index = self.get_slot_index_at_position(
                pygame.mouse.get_pos(), screen
            )

            for slot_index in range(columns*rows):
                column = slot_index % columns
                row = slot_index // columns

                slot_rect = pygame.Rect(
                    grid_x + column * (slot_width + slot_gap),
                    grid_y + row * (slot_height + slot_gap),
                    slot_width,
                    slot_height
                )

                #SLOT BG AND BORDER:
                pygame.draw.rect(screen, (25,62,76), slot_rect, border_radius = 5)
                if slot_index == hovered_index:
                    pygame.draw.rect(
                        screen, 
                        (255, 210, 90),
                        slot_rect,
                        4,
                        border_radius = 5
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        self.border_color,
                        slot_rect,
                        2,
                        border_radius = 5
                    )

                if slot_index < len(items) and slot_index != is_dragging:
                    #Item info
                    item = items[slot_index]

                    item_name = item.get("name", "Unknown")
                    item_rarity = item.get("rarity", "No Rarity")
                    item_category = item.get("category", "FISH")
                    is_locked = item.get("locked", False)

                    name_font = pygame.font.Font(None, 19)
                    detail_font = pygame.font.Font(None, 17)

                    #Helper Func
                    def fit_text(text, font, max_width):
                        text = str(text)

                        # Keep the original text if it already fits.
                        if font.size(text)[0] <= max_width:
                            return font.render(text, True, self.text_color)

                        # Shorten the text until it fits with an ellipsis.
                        while text and font.size(text + "...")[0] > max_width:
                            text = text[:-1]

                        return font.render(text + "...", True, self.text_color)

                    #Text Render:

                    name_text = fit_text(item_name,name_font,slot_width - 10)
                    rarity_text = fit_text(item_rarity,detail_font,slot_width - 10)
                    category_text = fit_text(item_category,detail_font,slot_width - 10)

                    screen.blit(name_text, name_text.get_rect(
                        center = (slot_rect.centerx, slot_rect.y + 20)
                    ))

                    screen.blit(rarity_text, rarity_text.get_rect(
                        center = (slot_rect.centerx, slot_rect.y + 43)
                    ))

                    screen.blit(category_text, category_text.get_rect(
                        center = (slot_rect.centerx, slot_rect.y + 65)
                    ))

                    if is_locked:
                        lock_text = self.info_font.render(
                            "LOCKED" , True, (255,190,70)
                        )
                        screen.blit(
                            lock_text ,
                            lock_text.get_rect(
                                center = (slot_rect.centerx, slot_rect.bottom - 8)
                            )
                        )

            #TEMPORARY FLOATING CARD:

            if(
                is_dragging is not None 
                and 0 <= is_dragging < len(items)
            ):
                dragged_item = items[is_dragging]

                mouse_x , mouse_y = pygame.mouse.get_pos()

                card_width = 160
                card_height = 65

                card_rect = pygame.Rect(
                    mouse_x + 14, mouse_y + 14,
                    card_width, card_height
                )
                pygame.draw.rect(
                    screen,
                    (25,62,76),
                    card_rect,
                    border_radius = 8
                )
                pygame.draw.rect(
                    screen,
                    (255,210,90),
                    card_rect,
                    2,
                    border_radius = 8
                )

                drag_name_font = pygame.font.Font(None, 23)
                drag_name_detail_font = pygame.font.Font(None, 19)

                drag_name = drag_name_font.render(
                    str(dragged_item.get("name", "Unknown")),
                    True,
                    self.text_color
                )

                drag_rarity = drag_name_detail_font.render(
                    str(dragged_item.get("rarity", "Common")),
                    True,
                    (255,210,90)
                )

                screen.blit(drag_name, (card_rect.x + 8, card_rect.y + 10))
                screen.blit(drag_rarity, (card_rect.x + 8,card_rect.y + 36))




            self.sort_dropdown.rect.topleft = (
                window_rect.x - self.sort_dropdown.rect.width - 25,
                window_rect.y + 20
            )
                    #Dropdown Menu
            self.sort_dropdown.draw(screen)

        else:
            #GEARS TAB:

            gear_area = pygame.Rect(
                window_rect.x + 25,
                window_rect.y + 120,
                self.width - 50,
                self.height -180
            )

            pygame.draw.rect(
                screen,
                (25,62,76),
                gear_area,
                border_radius = 10
            )

            pygame.draw.rect(
                screen,
                self.border_color,
                gear_area,
                2,
                border_radius = 10
            )

            gear_title = self.title_font.render(
                "GEARS:",
                True,
                self.text_color
            )
            gear_hint = self.info_font.render(
                "Your Erquipment will appear here (WIP)",
                True,
                self.text_color
            )
            screen.blit(
                gear_title,
                gear_title.get_rect(
                    center = (gear_area.centerx , gear_area.centery - 25)

                )
            )
            screen.blit(
                gear_hint,
                gear_hint.get_rect(
                    center = (gear_area.centerx , gear_area.centery + 20)
                )
            )

        close_hint = self.info_font.render(
            "Press TAB to close.",
            True,
            self.text_color
        )

        lock_hint = self. info_font.render(
            "Right click an item to lock/unlock." , 
            True,
            self.text_color
        )
        
        
        if self.active_tab == "Items":
            screen.blit(
                lock_hint,
                (window_rect.x + 25, window_rect.bottom - 60)
            )

        screen.blit(
            close_hint,
            (window_rect.x + 25, window_rect.bottom - 40)
        )

    def get_slot_index_at_position(self, mouse_pos, screen):
        window_rect = pygame.Rect( 0, 0, self.width, self.height)
        window_rect.center = screen.get_rect().center

        slot_width = 80
        slot_height = 80
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
