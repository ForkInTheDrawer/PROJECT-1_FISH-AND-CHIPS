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
            color = (
                button.hover_color

                if button.rect.collidepoint(local_mouse)
                else(button.color)
                )

            pygame.draw.rect(
                popup_surface,
                color,
                button.rect
            )

            text = self.button_font.render(
                button.text,
                True,
                button.text_color
            )

            popup_surface.blit(
                text, text.get_rect(center = button.rect.center)
            )

        scaled_surface = pygame.transform.smoothscale(
            popup_surface,
            self.draw_rect.size
        )

        screen.blit(scaled_surface, self.draw_rect)



    

class Sell_Notification(GUI):
    pass