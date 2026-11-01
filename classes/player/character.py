import pygame
import json
import os
from pathlib import Path

default_character = {
    "char_dimensions": (200, 200, 30, 50), # RECTANGLE DIMENSIONS + SIZE | (pos_X, pos_y, size_x, size_y)
    "char_speed": 200 # measured in pixels/second
    
}








class player:
    def __init__(
                self, 
                 name_val="john", 
                 gender_val="M", 
                 cash_val=0, 
                 chips_val=0, 
                 luck_val=0, 
                 walkspeed=default_character["char_speed"],
                 dimensions=default_character["char_dimensions"]
                 ):

        
        self.character= pygame.Rect(dimensions)
        self.name = name_val
        self.gender = gender_val
        self.cash = cash_val
        self.chips = chips_val
        self.luckMult = luck_val
        self.walkspeed = walkspeed
        
        self.inventory = None        

    #----------------
        #NOTE: DO THESE LATER ONCE YOU UNDERSTAND HOW TO IMPLEMENT THEM:
        # self.gender = gender
        # self.cash = cash
        # self.chips = chips
        # self.luck = luck

    #NOTE: "STARTING HERE, IT PULLS inventory_storage.json" 
        save_folder = Path(os.getenv("LOCALAPPDATA")) / "Fish n Chips" / "saves"
        save_folder.mkdir(parents=True, exist_ok=True)

        inventory_path = save_folder / "inventory_storage.json"

        if inventory_path.exists():
            with inventory_path.open(encoding="utf-8") as file:
                inventory_dict = json.load(file)
        else:
            inventory_dict = {
                "maximum_slots": 10,
                "plr_inv": []
            }

            with inventory_path.open("w", encoding="utf-8") as file:
                json.dump(inventory_dict, file, indent=4)

        self.inventory = inventory_dict
     
    #----------------

    def save_inventory(self):
        save_folder = Path(os.getenv("LOCALAPPDATA")) / "Fish n Chips" / "saves"
        save_folder.mkdir(parents=True, exist_ok=True)

        inventory_path = save_folder / "inventory_storage.json"

        with inventory_path.open("w", encoding="utf-8") as file:
            json.dump(self.inventory, file, indent=4)

    def add_to_inventory(self, item):
        items = self.inventory["plr_inv"]

        if len(items) >= self.inventory["maximum_slots"]:
            return False

        items.append(item)
        self.save_inventory()
        return True



        





# class obstacles:
#     def __init__(self, hitbox, shape)
