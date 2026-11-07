import pygame
from classes.ui_handling.button import Button
from classes.fishing.scrap_mutations import SCRAP_MUTATIONS
from classes.animations import easing
from classes.animations.animation import Animation

default_config = {
    "proximity prompt": {
        "size" : (500,100) ,
        "position" : (350 , 575),
        
    },
}


class GUI():
    def __init__(self, position, size, fill_color):
        
       self.rect = pygame.Rect(position, size)
       self.fill_color = fill_color
       


    def draw(self, screen):
        pygame.draw.rect(screen,self.fill_color, self.rect)

    @classmethod

    def proximity_prompt(
        cls,
        action, position=(350, 575),
        size=(500, 100),
        key=pygame.K_e,
    ):
        return ProximityPrompt(action, position, size, key)







class ProximityPrompt(GUI):

    def __init__(self, action, position, size, key):

        super().__init__(position, size, (30,30,30))
        self.key = key
        self.font = pygame.font.Font(None, 32)
        self.label = f"Press {pygame.key.name(key).upper()} to {action}"

        self.scale_animation = None

    def start_animation(self):
        self.scale_animation = Animation(
            start_val = 0.50,
            end_val = 1.0,
            duration = 0.4,
            easing_function = easing.ease_out_back
        )

    



    def draw(self, screen, dt=0):

        scale = 1.0

        if self.scale_animation is not None:
            scale = self.scale_animation.update(dt)

            if self.scale_animation.finished_status:
                self.scale_animation = None
                scale = 1.0


        popup_surface = pygame.Surface(self.rect.size , pygame.SRCALPHA)

        pygame.draw.rect(
            popup_surface,
            self.fill_color,
            popup_surface.get_rect()
        )
        text = self.font.render(self.label, True, (255,255,255))

        popup_surface.blit(
            text,
            text.get_rect(center = popup_surface.get_rect().center)
        )

        scaled_size = (
            max(1, round(self.rect.width * scale)),
            max(1, round(self.rect.height * scale)),
        )
        scaled_surface = pygame.transform.smoothscale(popup_surface, scaled_size)

        screen.blit(
        scaled_surface,
        scaled_surface.get_rect(center = self.rect.center)
        )



    
class InventoryFull(GUI):   #NOTE: WORK ON THIS SO THAT THE "INVENTORY FULL" WILL BE IN THE ____

    def __init__ (self, position=(350, 575), size=(500,100)):
        super().__init__(position , size, (30, 30, 30))

        self.font = pygame.font.Font(None, 36)

    def draw(self,screen):
        super().draw(screen)
        text = self.font.render("Inventory Full! Sell to fish again.", True, (255,255,255))
        screen.blit(text, text.get_rect(center =self.rect.center))

class InventoryWindow:
    def __init__(self, size = (760, 560)):
        self.width, self.height = size

        self.background_color = (16,43,58)
        self.border_color = (255, 255, 255)
        self.text_color = (244,231,197)

        self.title_font = pygame.font.Font(None, 48)
        self.info_font = pygame.font.Font(None, 26)

    def draw(self,screen , inventory):

        overlay = pygame.Surface(screen.get_size() , pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        screen.blit(overlay, (0,0))

        window_rect = pygame.Rect(
            0,0,
            self.width, self.height
        )

        window_rect.center = screen.get_rect().center

        pygame.draw.rect(
            screen, self.background_color, window_rect
        )
        pygame.draw.rect(
            screen, self.border_color, window_rect, 3
        )

        #Window Title
        title = self.title_font.render("INVENTORY", True, self.text_color)
        screen.blit(title, (window_rect.x + 25, window_rect.y + 20))

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
            pygame.draw.rect(screen, (25,62,76), slot_rect)
            pygame.draw.rect(screen, self.border_color, slot_rect, 2)

            if slot_index < len(items):
                #Item info
                item = items[slot_index]

                item_name = item.get("name", "Unknown")
                item_rarity = item.get("rarity", "No Rarity")
                item_category = item.get("category", "FISH")

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

        close_template = self.info_font.render(
            "Press TAB to close.",
            True,
            self.text_color
        )

        screen.blit(
            close_template,
            (window_rect.x + 25, window_rect.bottom - 40)
        )








class FishPopUp(GUI):   
    def __init__(self,caught_fish , position=(350,260), size=(500,280), skip_key=pygame.K_SPACE):
        super().__init__(position,size,(30,30,30))
        self.title_font = pygame.font.Font(None, 42)
        self.body_font = pygame.font.Font(None, 30)
        self.name = caught_fish.get('name', 'Unknown Fish')

        category = caught_fish.get("category" , "FISH")






        if category == "STONES":
            self.details = [
                f'Tier: {caught_fish.get("rarity", "Unknown")}',
                f'Price: {caught_fish.get("base_price", 0):,.2f} Chips',
                f'Stats: (PLACEHOLDER)'
            ]

        elif category == "SCRAP":
            mutation = caught_fish.get("mutation")
            base_price = caught_fish.get("price", 0)

            if mutation == "Glitched":
                selling_value = base_price
                currency = "Chips"

            elif mutation in SCRAP_MUTATIONS:
                mutation_data = SCRAP_MUTATIONS[mutation]
                selling_value = base_price * mutation_data.get("price_multiplier", 1)
                currency = "Coins"

            else:
                selling_value = base_price
                currency = "Coins"
            self.details =[
                f'Mutation: {mutation or "None"}',
                f'Price: {"$" if currency == "Coins" else ""}{selling_value:,.2f} {currency if currency =="Chips" else ""}',

            ]
            




            

        else: #FOR FISH
            self.details = [
                f'Rarity: {caught_fish.get("rarity", "Unknown")}',
                f'Mutation: {caught_fish.get("mutation", "None")}',
                f'Weight: {caught_fish.get("weight", 0):.2f} kg'
            ]



        self.skip_key = skip_key


        self.gui_cooldown(4)                   #NOTE: GUI COOLDOWN FOR FISH RESULTS.






        for color_key in ("COLOR_1" , "COLOR_2"):
            if color_key in caught_fish:
                self.details.append(
                    f"Color{color_key[-1]} : {caught_fish[color_key]}"
                )





    def gui_cooldown(self, cooldown=1.0):

        self.cooldown_start = pygame.time.get_ticks()
        self.cooldown_ms = cooldown * 1000









    def draw(self , screen): #NOTE: FOR RENDERING

        if pygame.time.get_ticks() - self.cooldown_start >= self.cooldown_ms:
            return

        super().draw(screen)
        title = self.title_font.render(self.name, True , (255,220,100),)
        screen.blit(title, title.get_rect(midtop=(self.rect.centerx , self.rect.y + 20)))


        for index, detail in enumerate(self.details):
            text = self.body_font.render(detail, True, (255,255,255))
            screen.blit(text , (self.rect.x + 30, self.rect.y + 85 + index * 35))



        #--------------------------------------- FOR FISHING SYSTEM
        #NOTE: BASICALLY SAYING THE COUNTDOWN
        remaining_ms = self.cooldown_ms - (
            pygame.time.get_ticks() - self.cooldown_start
        )
        remaining_seconds = max(0, (remaining_ms + 999) // 1000)

        countdown = self.body_font.render(
            f"Fish again in {remaining_seconds} seconds. ",
            True,
            (200,200,200)
        )

        skip_countdown = self.body_font.render(    #NOTE: SKIP COUNTDOWN
            f"Press {pygame.key.name(self.skip_key).upper()} to skip.",
            True,
            (200,200,200)
        )
        screen.blit(
            countdown, countdown.get_rect(
                center = (self.rect.centerx , self.rect.bottom - 35)
            )
        )
        screen.blit(
            skip_countdown , skip_countdown.get_rect(
                center = (self.rect.centerx , self.rect.bottom -  10)
            )
        )




class Sell_Confirmation(GUI):
    def __init__ (self, item_name):
        super().__init__(
            position = (300,280),
            size = (600,240),
            fill_color = (30,30,30)
        )

        self.item_name = item_name
        self.font = pygame.font.Font(None, 35)
        self.button_font = pygame.font.Font(None,32)

        self.yes_button = Button( 
            "YES", (255,255,255), 
            pygame.Rect(100,140,150,55), 
            (49,132,92), (70,160,110))

        self.no_button = Button("NO", (255,255,255), 
        pygame.Rect(320,140,150,55), 
        (169,67,67), (200,85,85))

        self.scale_animation = Animation(
            start_val = 0.85,
            end_val = 1.0,
            duration = 0.4,
            easing_function = easing.ease_out_back
        )
        
        self.current_scale = 0.85
        self.draw_rect = self.rect.copy()

        self.button_scales = {
            "YES" : 1.0, "NO" : 1.0
        }

        self.button_hover_speed = 12
        self.button_hover_scale = 1.08


    def draw(self, screen, dt):
        if self.scale_animation is not None:
            self.current_scale = self.scale_animation.update(dt)

            if self.scale_animation.finished_status:
                self.scale_animation = None
                self.current_scale = 1.0


        popup_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            popup_surface,
            self.fill_color,
            popup_surface.get_rect()
        )

        title = self.font.render(
            f'Sell {self.item_name}?',
            True,
            (255,255,255)
        )

        popup_surface.blit( title, title.get_rect(center = (300,90)))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        scaled_width = round(self.rect.width * self.current_scale)
        scaled_height = round(self.rect.height * self.current_scale)

        self.draw_rect = pygame.Rect(
            0,0, scaled_width, scaled_height
        )

        self.draw_rect.center = self.rect.center

        local_mouse = (
            (mouse_x - self.draw_rect.left) / self.current_scale,
            (mouse_y - self.draw_rect.top) / self.current_scale
        )

        for button in (self.yes_button, self.no_button):

            button_hovered = button.rect.collidepoint(local_mouse)

            target_scale = (self.button_hover_scale if button_hovered else 1.0)

            current_scale = self.button_scales[button.text]

            current_scale += (target_scale - current_scale) * min(1.0, self.button_hover_speed *dt)

            self.button_scales[button.text] = current_scale

            color = button.hover_color if button_hovered else button.color
            scaled_width = round(button.rect.width * current_scale)
            scaled_height = round(button.rect.height * current_scale)

            scaled_button_rect = pygame.Rect(
                0,0, scaled_width, scaled_height
            )
            scaled_button_rect.center = button.rect.center

            pygame.draw.rect(
                popup_surface,
                color,
                scaled_button_rect,
                border_radius = 6
            )

            text = self.button_font.render(
                button.text, True, button.text_color
            )

            scaled_text = pygame.transform.smoothscale(
                text, (
                    max(1, round(text.get_width() * current_scale)),
                    max(1, round(text.get_height() * current_scale))
                )
            )

            popup_surface.blit(
                scaled_text, scaled_text.get_rect(center = scaled_button_rect.center)
            )

            scaled_surface = pygame.transform.smoothscale(
                popup_surface, self.draw_rect.size
            )

            screen.blit(scaled_surface, self.draw_rect)



class Sell_Notification(GUI):
    def __init__(self):

        self.notifications = []
        self.exiting_notifications = []

        self.font = pygame.font.Font(None, 25)

        self.max_notifications = 5
        self.notification_width = 340
        self.notification_height = 64
        self.notification_gap = 10

        self.margin_right = 24
        self.margin_bottom = 24

        self.idle_time = 0
        self.fade_progress = 0

        self.fade_delay = 3.0
        self.fade_duration = 0.5
        self.overflow_fade_duration = 0.3

    def add_notif(self, fish_name= None, price= None, currency= None, message = None):

        self.idle_time = 0
        self.fade_progress = 0


        if len(self.notifications) >= self.max_notifications:
            oldest = self.notifications.pop(0)

            self.exiting_notifications.append( {
                "name" : oldest["name"],
                "price" : oldest["price"],
                "currency" : oldest["currency"],
                "message" : oldest.get("message"),
                "y" : oldest["y"],
                "alpha" : 255,
                "elapsed" : 0
            } )

        new_notification = {
            "name" : fish_name,
            "price" : price,
            "currency" : currency,
            "message" : message,
            "y" : pygame.display.get_surface().get_height() + 20
        }

        self.notifications.append(new_notification)


    def update(self, dt):
        if self.notifications:
            self.idle_time += dt

            if self.idle_time >= self.fade_delay:
                self.fade_progress = min(
                    1.0,
                    self.fade_progress + dt / self.fade_duration
                )

                if self.fade_progress >= 1.0:
                    self.notifications.clear()
                    self.fade_progress = 0
                    self.idle_time = 0


        for notification in self.exiting_notifications [:]:

            notification["elapsed"] += dt

            progress = min(
                1.0,
                notification ["elapsed"] / self.overflow_fade_duration
            )

            notification["alpha"] = round(255 * (1 - progress))

            if progress >= 1.0:
                self.exiting_notifications.remove(notification)

                #STACK POSITIONS
        screen_height = pygame.display.get_surface().get_height()

        bottom_y = (
            screen_height - self.margin_bottom - self.notification_height
        )

        stack_spacing = (
            self.notification_height + self.notification_gap
        )

        for index, notification in enumerate(self.notifications):
            target_y = bottom_y - (
                len(self.notifications) - 1 - index
            ) * stack_spacing

            notification["y"] += (
                target_y - notification["y"]
            ) * min(1.0, 12 * dt)

    def draw_notif(self, screen, notification, alpha):
        notification_surface = pygame.Surface(
            (self.notification_width, self.notification_height),
            pygame.SRCALPHA
        )

        background = (20,45,55)
        border = (115, 226, 208)
        

        pygame.draw.rect(
            notification_surface,
            border,
            notification_surface.get_rect(),
            width = 2,
            border_radius = 8
        )

        if notification.get("message"):
            message = notification["message"]
        else:
            message = (
                f"You sold {notification['name']} for "
                f"{notification['price']:,.2f} "
                f"{notification['currency']}!"
    )


        #WRAP TEXT MAX
        max_text_width = self.notification_width - 24
        words = message.split(" ")

        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()

            if self.font.size(test_line)[0] <= max_text_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)

                current_line = word
        if current_line:
            lines.append(current_line)

        line_height = self.font.get_linesize()
        total_text_height = len(lines) * line_height

        start_y = (
            self.notification_height - total_text_height
        ) // 2

        for index, line in enumerate(lines):
            text = self.font.render(line, True, (255,255,255))

            text_rect = text.get_rect(
                center = (self.notification_width // 2,
                          start_y + index * line_height + line_height //2
                          )
            )

            notification_surface.blit(text, text_rect)


        notification_surface.set_alpha(alpha)

        x = screen.get_width() - self.margin_right - self.notification_width
        screen.blit (notification_surface, (x, round(notification["y"])))

    def draw(self,screen):
        alpha = round(255 * (1 - self.fade_progress))

        for notification in self.notifications:
            self.draw_notif(screen, notification, alpha)

        for notification in self.exiting_notifications:
            self.draw_notif(screen, notification, notification["alpha"])