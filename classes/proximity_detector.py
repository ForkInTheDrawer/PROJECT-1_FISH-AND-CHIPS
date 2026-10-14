


import pygame

class proximity:
    def __init__(self, coords, distance, Action_Name=None, Object_Name=None, keybind=pygame.K_e):

        self.position = coords #<-its a tuple
        self.max_distance = distance[0] #how far can the player detect
        self.min_distance = distance[1] #ofc
        self.ActionName = Action_Name
        self.ObjectName = Object_Name
        self.kb = keybind



    def is_in_range(self, player_rect):
        #Distance from placer center to interaction point.

        player_center = pygame.Vector2(player_rect.center)
        target_position = pygame.Vector2(self.position)

        distance = player_center.distance_to(target_position)

        return self.min_distance <= distance <= self.max_distance



    def triggered_event(self, event, player_rect):

        #TRIGGERS ONLY WHEN THE CORRECT KEY IS APPLIED.
        return(
            event.type == pygame.KEYDOWN
            and event.key == self.kb
            and self.is_in_range(player_rect)
        )


fishing_proximity = proximity((0,0),(10,0), "Fish", "fishingrod!!", pygame.key.key_code("space"))
shop_proximity = proximity( (0,0), (10,20), "'E' Buy Gear" , None , pygame.key.key_code("e"))