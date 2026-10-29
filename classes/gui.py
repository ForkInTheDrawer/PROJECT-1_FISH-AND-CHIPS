import pygame

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

    def draw(self, screen):
        super().draw(screen)
        text = self.font.render(self.label, True, (255, 255 ,255))
        screen.blit(text, text.get_rect(center=self.rect.center))

    
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
                f'Price: ${caught_fish.get("base_price", 0):,.2f}',
                f'Stats: (PLACEHOLDER)'
            ]

        elif category == "SCRAP":
            self.details = [
                f'Price: $ {caught_fish.get('price', 0):.2f}'
            ]

        else: #FOR FISH
            self.details = [
                f'Rarity: {caught_fish.get('rarity', 'Unknown')}',
                f'Mutation: {caught_fish.get('mutation', 'None')}',
                f'Weight: {caught_fish.get('weight', 0)} kg'
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

        self.yes_button = pygame.Rect(400,200, 150,55)
        self.no_button = pygame.Rect(650,200,150,55)

    def draw(self, screen):
        super().draw(screen)
        title = self.font.render(
            f"Sell {self.item_name}?",
            True,
            (255,220,100)
        )

        screen.blit(
            title, title.get_rect(center = (self.rect.centerx,370))
        )


        pygame.draw.rect(screen, (49,132, 92), self.yes_button)

        pygame.draw.rect(screen, (169,67,67), self.no_button)

        yes_text = self.button_font.render(
            "YES", True, (255,255,255)
        )
        no_text = self.button_font.render(
            "NO", True, (255,255,255)
        )

        screen.blit(
            yes_text, yes_text.get_rect(center = self.yes_button.center)
        )

        screen.blit(
            no_text, no_text.get_rect(center = self.no_button.center)
        )

    

