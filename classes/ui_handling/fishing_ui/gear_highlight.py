import pygame

class GearHighlight:

    def __init__(self):
        self.pulse_duration = 1200


    def draw(
      self,
      screen,
      inventory_window,
      inventory,
      dragging_inventory_index = None,
      dragging_toolbar_index = None,
      toolbar_slot_rects = None      
    ):

        #Highlights only while gear tab is open.

        if inventory_window.active_tab != "Gear":
            return

        dragged_item = None

        if dragging_inventory_index is not None:
            items = inventory["plr_inv"]

            if 0 <= dragging_inventory_index < len(items):
                dragged_item = items[dragging_inventory_index]


        elif dragging_toolbar_index is not None:
            slots = inventory["toolbar_slots"]

            if 0 <= dragging_toolbar_index < len(slots):
                dragged_item = slots[dragging_toolbar_index]

        if dragged_item is None:
            return

        category = str(dragged_item.get("category", "")).upper()

        pulse_phase = (
            pygame.time.get_ticks() % self.pulse_duration
        ) / self.pulse_duration

        pulse_amount = 1 - abs(2 * pulse_phase - 1)


        pulse_color = (
            255,
            165 + int(65 * pulse_amount),
            25
        )


        #equipment categories + slots


        equipment_slots = {
            "HEAD" : 0,
            "BODY" : 1,
            "RING" : 2,
            "BOOTS" : 3
        }
        
        #Matching valid slot system

        if category in equipment_slots:

            window_rect = pygame.Rect(
                0,0,
                inventory_window.width,
                inventory_window.height
            )

            window_rect.center = screen.get_pos().center

            panel_rect = pygame.Rect(

                window_rect.x + 25,
                window_rect.y + 120,
                240,
                350
            )
            slot_width = 68
            slot_height = 65
            slot_gap = 8

            slot_start_y = panel_rect.centery - (
                (4 * slot_height + 3 * slot_gap) // 2
            )

            slot_index = equipment_slots[category]

            slot_rect = pygame.Rect(
                panel_rect.x + 20,
                slot_start_y + slot_index * (slot_height + slot_gap),
                slot_width,
                slot_height
            )


            pygame.draw.rect(
                screen,
                pulse_color,
                slot_rect,
                4,
                border_radius= 7
            )

        #Fishing rod highlights

        elif category == "FISHING_ROD" : 

            if toolbar_slot_rects and len(toolbar_slot_rects) > 0:
                pygame.draw.rect(
                    screen,
                    pulse_color,
                    toolbar_slot_rects[0],
                    4,
                    border_radius= 7
                )