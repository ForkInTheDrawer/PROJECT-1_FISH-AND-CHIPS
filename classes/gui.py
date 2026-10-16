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
        action,
        position=(350, 575),
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


