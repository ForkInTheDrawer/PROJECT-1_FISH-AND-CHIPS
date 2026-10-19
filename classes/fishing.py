import random
import pygame



class Fishing: 
    def __init__(self, fish_data): #Gets data ready
        self.fish_data = fish_data
        
        self.is_fishing = False
        self.is_casting = False
        self.start_time = 0
        self.duration = 0
        self.cast_time_prompt = 0


    def choose_fish(self): #Readys
        fish_names = list(self.fish_data)

        fish_weights = [
            self.fish_data[name]["Weight"]
            for name in fish_names
        ]

        name = random.choices(
            fish_names,
            weights = fish_weights,
            k=1
        )[0]
        details = self.fish_data[name]
        caught_fish = {
            "name": name,
            "type": random.choice(details["Type"]),
            "mutation": random.choice(details["Mutation"])
        }

        for color in ("Color_1",  "Color_2"):
            if color in details:
                caught_fish[color.upper()] = random.choice(details[color])

        return caught_fish









    def start(self):
        if self.is_fishing or self.is_casting:
            return

        
        self.is_casting = True
        self.cast_time_prompt = pygame.time.get_ticks() + 200
        


    def update(self):

        if not self.is_fishing and not self.is_casting:
            return False

        current_time = pygame.time.get_ticks()

        #Wait for 0.2 Seconds before printing casting (FOR ANIMATION)
        if self.is_casting is True and current_time >= self.cast_time_prompt:

            print("Casting Bait...")

            self.cast_time_prompt = current_time + 1500
            self.is_casting = "waiting"


        #2.5 Seconds before fishing starts

        elif self.is_casting == "waiting" and current_time >= self.cast_time_prompt:

            self.is_casting = False
            self.is_fishing = True
            self.start_time = current_time
            self.duration = random.uniform(2,4)

            print('Fishing Started! Catch Time:',
                  round(self.duration , 1),
                  "seconds."
                  )

    


        #Check if fish is caught:

        elif self.is_fishing:
            elapsed_time = (current_time -self.start_time) / 1000

            if elapsed_time >= self.duration:
                self.is_fishing = False
                return True


        return False





#NOTE: THIS IS FOR THE FISHES!!!!!!!!



class fish_rarity():
    def __init__ (self, rarity, price, weight):
        self.rarity = rarity
        self.price = price
        self.weight = weight


    

        #Placeholder for fish types


