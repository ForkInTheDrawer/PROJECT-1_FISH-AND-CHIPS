import random
import pygame


class Fishing:
    def __init__(self):
        self.is_fishing = False
        self.start_time = 0
        self.duration = 0


    def start(self):
        if self.is_fishing:
            return

        self.is_fishing = True
        self.start_time = pygame.time.get_ticks()
        self.duration = random.uniform(1,4)

        print("Fishing Started! Catch Time:" , round(self.duration, 1) , "seconds.")

    def update(self):
        
        if not self.is_fishing:
            return False

        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

        if elapsed_time >= self.duration:
            self.is_fishing = False
            return True

        return False