import pygame
from classes.ui_handling.gui import GUI

class InventoryFull(GUI):   #NOTE: WORK ON THIS SO THAT THE "INVENTORY FULL" WILL BE IN THE ____

    def __init__ (self, position=(350, 575), size=(500,100)):
        super().__init__(position , size, (30, 30, 30))

        self.font = pygame.font.Font(None, 36)

    def draw(self,screen):
        super().draw(screen)
        text = self.font.render("Inventory Full! Sell to fish again.", True, (255,255,255))
        screen.blit(text, text.get_rect(center =self.rect.center))
