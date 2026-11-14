import pygame


from classes.ui_handling.button import Button, DropdownMenu
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
       


    def draw(self, screen, dt : float = 0.0):
        pygame.draw.rect(screen,self.fill_color, self.rect)

    @classmethod

    def proximity_prompt(
        cls,
        action, position=(350, 575),
        size=(500, 100),
        key=pygame.K_e,
    ):

        from classes.ui_handling.fishing_ui.proximity_prompt import ProximityPrompt

        return ProximityPrompt(action, position, size, key)

