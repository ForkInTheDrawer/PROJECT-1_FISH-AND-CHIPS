import pygame

default_config = {
    "proximity prompt": {
        "size" : (10,10) ,
        "position" : (30,30),
        
    },
}


class gui():
    def __init__(self, pos: tuple, size: tuple, fill_color, border=False ,border_width=2):
        
        self.size = size
        self.fill_color = fill_color
        self.pos = pos
        self.border = border
        self.border_width = border_width
       
        if border is True:
            self.border_width = border_width
        

    def draw(self, screen):
        prompt = pygame.Rect(self.pos , self.size)
        pygame.draw.rect(screen, self.fill_color, prompt)



    def proxi_prompt(self, keybind_icon=pygame.K_e):
        proximity = pygame.Rect(default_config["proximity prompt"]["position"], default_config["proximity prompt"]["size"])





