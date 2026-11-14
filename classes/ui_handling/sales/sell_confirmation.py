import pygame

from classes.ui_handling.gui import GUI
from classes.ui_handling.button import Button
from classes.animations import easing
from classes.animations.animation import Animation


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
