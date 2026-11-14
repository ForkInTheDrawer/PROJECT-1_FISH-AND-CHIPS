import pygame

from classes.ui_handling.gui import GUI
from classes.fishing.scrap_mutations import SCRAP_MUTATIONS
from classes.animations import easing
from classes.animations.animation import Animation



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

        self.scale_animation = Animation(
            start_val= 0.75,
            end_val= 1.0,
            duration = 0.45,
            easing_function= easing.ease_out_back
        )




        for color_key in ("COLOR_1" , "COLOR_2"):
            if color_key in caught_fish:
                self.details.append(
                    f"Color{color_key[-1]} : {caught_fish[color_key]}"
                )





    def gui_cooldown(self, cooldown=1.0):

        self.cooldown_start = pygame.time.get_ticks()
        self.cooldown_ms = cooldown * 1000









    def draw(self , screen, dt : float = 0.0): #NOTE: FOR RENDERING

        if pygame.time.get_ticks() - self.cooldown_start >= self.cooldown_ms:
            return

       # POPUP ANIMATION:
        if self.scale_animation is not None:
            self.current_scale = self.scale_animation.update(dt)

            if self.scale_animation.finished_status:
                self.scale_animation = None
                self.current_scale = 1.0

        #POPUP SURFACE:

        popup_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        pygame.draw.rect(
            popup_surface,
            self.fill_color,
            popup_surface.get_rect(),
            border_radius = 5
        )

        #TITLE:

        title = self.title_font.render(
            self.name,
            True,
            (255,220,100)
        )

        popup_surface.blit(
            title,
            title.get_rect(midtop = (self.rect.width // 2, 20))
        )

        #DETAILS:

        for index, detail in enumerate(self.details):
            text = self.body_font.render(detail, True, (255,255,255))

            popup_surface.blit(
                text,
                (30,85 + index * 35)
            )

        #COUNTDOWN TIMER:

        remaining_ms = self.cooldown_ms- (
            pygame.time.get_ticks() - self.cooldown_start
        )

        remaining_seconds = max(0, (remaining_ms + 999) // 1000)

        countdown = self.body_font.render(
            f"Fish again in {remaining_seconds} seconds.",
            True,
            (200,200,200)
        )
        skip_countdown = self.body_font.render(
            f"Press {pygame.key.name(self.skip_key).upper()} to skip.",
            True,
            (200,200,200)
        )
        popup_surface.blit(
            countdown,
            countdown.get_rect(
                center = (self.rect.width // 2, self.rect.height - 35)
            )
        )
        popup_surface.blit(
            skip_countdown,
            skip_countdown.get_rect(
                center=(self.rect.width // 2, self.rect.height - 10)
            )
        )
        #SCALE:
        scaled_size = (
            max(1, round(self.rect.width * self.current_scale)),
            max(1, round(self.rect.height * self.current_scale))
        )

        scaled_surface = pygame.transform.smoothscale(
            popup_surface, scaled_size
        )

        screen.blit(scaled_surface, scaled_surface.get_rect(center = self.rect.center))
