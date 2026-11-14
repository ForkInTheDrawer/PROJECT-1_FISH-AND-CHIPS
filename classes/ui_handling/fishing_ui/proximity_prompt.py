import pygame

from classes.ui_handling.gui import GUI
from classes.animations import easing
from classes.animations.animation import Animation



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
            popup_surface.get_rect(),
            border_radius = 10
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