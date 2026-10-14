import pygame

default_character = {
    "dimensions": (200, 200, 30, 50) 
}



class player:
    def __init__(self, name_val, gender_val, cash_val, chips_val, luck_val, walkspeed, character=None):

        if character is None:
            self.character = default_character
        else:
            self.character = character

        self.name = name_val
        self.gender = gender_val
        self.cash = cash_val
        self.chips = chips_val
        self.luckMult = luck_val
        self.walkspeed = walkspeed
        


        #NOTE: DO THESE LATER ONCE YOU UNDERSTAND HOW TO IMPLEMENT THEM:
        # self.gender = gender
        # self.cash = cash
        # self.chips = chips
        # self.luck = luck
    def get_money(self, name):
        
        print(f"{self.name}")
        





# class obstacles:
#     def __init__(self, hitbox, shape)
