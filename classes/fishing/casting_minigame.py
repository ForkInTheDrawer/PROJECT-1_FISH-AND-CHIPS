import pygame
import random


class CastingMinigame:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        #Meter dimentions and pos:

        self.bar_width = min(600, screen_width - 80)
        self.bar_height = 30
        self.bar_x = (screen_width - self.bar_width) // 2
        self.bar_y = screen_height // 2 + 160

        self.green_width = self.bar_width * random.uniform(0.08,0.20)
        self.yellow_width = round(self.bar_width * 0.14)

        self.indicator_x = float(self.bar_x)
        self.indicator_speed = random.randint(500, 1000)
        self.direction = 1

        #minigame

        self.finished = False
        self.cancelled = False
        self.result = None

        self.font = pygame.font.Font(None, 30)

        self.randomise_zones()

    def randomise_zones(self):

        self.green_width = round(self.bar_width * random.uniform(0.08, 0.20))

        available_width = (
            self.bar_width - self.green_width - (self.yellow_width * 2)
        )

        self.green_x = (
        self.bar_x
        + self.yellow_width
        + random.randint(0, available_width)
        )
        self.yellow_left_x = self.green_x - self.yellow_width
        self.yellow_right_x = self.green_x + self.green_width


    def update(self, dt):
        if self.finished:
            return

        self.indicator_x += (
            self.indicator_speed * self.direction * dt
        )


        left_edge = self.bar_x

        right_edge = self.bar_x + self.bar_width

        if self.indicator_x >= right_edge:
            self.indicator_x = right_edge
            self.direction = -1

        elif self.indicator_x <= left_edge:
            self.indicator_x = left_edge
            self.direction = 1


    def handle_event(self, event):

        if event.type != pygame.KEYDOWN or self.finished:
            return


        if event.key == pygame.K_ESCAPE:
            self.cancelled = True
            self.finished = True


        elif event.key == pygame.K_e:
            self.stop_indicator()

    def stop_indicator(self):

        pos = self.indicator_x

        if self.green_x <= pos <= self.green_x + self.green_width:
            self.result = 1.10

        elif(
            self.yellow_left_x <= pos <= self.yellow_left_x + self.yellow_width
            or
            self.yellow_right_x <= pos <= self.yellow_right_x + self.yellow_width
        ):
            self.result = 1.0


        else:
            self.result = 0.80


        self.finished = True

    def draw(self, screen):

        bar_rect = pygame.Rect(
            self.bar_x,
            self.bar_y,
            self.bar_width,
            self.bar_height
        )

        #Red Bg
        pygame.draw.rect(screen, (220, 60, 60), bar_rect)

        #Yellow Zone

        pygame.draw.rect(
            screen,
            (240,210,60),
            (
                self.yellow_left_x,
                self.bar_y,
                self.yellow_width,
                self.bar_height
            )
        )

        pygame.draw.rect(
            screen,
            (240, 210, 60),
            (
                self.yellow_right_x,
                self.bar_y,
                self.yellow_width,
                self.bar_height
            )
        )

        #Green Zone

        pygame.draw.rect(
            screen,
            (60,200,90),
            (
                self.green_x,
                self.bar_y,
                self.green_width,
                self.bar_height
            )
        )


        #Moving Line

        pygame.draw.line(
            screen,
            (255,255,255),
            (int(self.indicator_x), self.bar_y - 8),
            (int(self.indicator_x), self.bar_y + self.bar_height + 8),
            4
        )

        #Tips:

        instructions = self.font.render(
            "Press E to stop | ESC to Cancel.",
            True,
            (255,255,255)
        )

        screen.blit(
            instructions,
            instructions.get_rect(
                center = (self.screen_width // 2, self.bar_y + 65)
            )
        )