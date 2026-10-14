import pygame

class proximity:
    def __init__(self, coords, distance, Action_Name: str=None, Object_Name: str=None, keybind=pygame.key.key_code("e")):
        self.position = coords #<-its a tuple
        self.max_distance = distance[0] #how far can the player detect
        self.min_distance = distance[1] #ofc
        self.ActionName = Action_Name
        self.ObjectName = Object_Name
        self.kb = keybind


fishing_proximity = proximity((0,0),(10,0), "Fish", "fishingrod!!", pygame.key.key_code("space"))