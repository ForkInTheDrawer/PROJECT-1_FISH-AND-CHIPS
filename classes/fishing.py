import random
import pygame
from . import fish_prices
from enum import Enum


class Item_Category(Enum):
    FISH = "FISH"
    SCRAP = "SCRAP"
    STONE = "STONES"


class Fishing: 
    def __init__(self, fish_data, scrap_data, stones_data): #Gets data ready
        self.fish_data = fish_data
        self.scrap_data = scrap_data
        self.stones_data = stones_data


        self.debug_mode = False #NOTE: DEBUG MODE

        self.is_fishing = False
        self.is_casting = False
    
        self.start_time = 0
        self.duration = 0
        self.cast_time_prompt = 0


        
    def choose_category(self): #Chooses category to get. 
        return random.choices(
            list(Item_Category),
            weights = [80,15,5],
            k = 1
    )[0]

    def choose_stone_rarity(self): #Chooses stone rarity
        stone_rarities = [
            "Honed",
            "Tidebound",
            "Soulbound",
            "Aetherbound"
        ]
        chances = [99.4, 0.5, 0.05, 0.05]
        return random.choices(stone_rarities, weights = chances, k = 1)[0]

    def choose_item_name(self, category): #Checks for correct dictionary

        if category == Item_Category.FISH:
            item_data = self.fish_data
            item_names = list(self.fish_data)
            item_weights = [
                item_data[name]['Weight']
                for name in item_names
            ]
            return random.choices(
             item_names,
            weights = item_weights,
            k = 1
            )[0]
    

        elif category == Item_Category.SCRAP:
             return random.choice(list(self.scrap_data))

        else:
            return random.choice(list(self.stones_data))

    
    def choose_fish(self): #Readys the fish to be caught

        category = self.choose_category()
        item_name = self.choose_item_name(category)

        if category == Item_Category.SCRAP:
            return{
                "name" : item_name,
                "category" : category.value,
                "price" : self.scrap_data[item_name]["PRICE"]
            }
        elif category == Item_Category.STONE:
            rarity = self.choose_stone_rarity()

            base_price = self.stones_data[item_name]["PRICE"]

            return{
                "name" : item_name,
                "category" : category.value,
                "rarity" : rarity,
                "base_price" : base_price
            }


        name = item_name
        details = self.fish_data[name]
        
        rarity_weights = [60, 20, 10.5, 8, 0.999, 0.5, 0.001]

        fish_rarity = random.choices(
        details["Rarity"],
        weights = rarity_weights,
        k=1
        )[0]
        


        #--------------------------MUTATIONS--------------

        if self.debug_mode:
            mutation_chances = [1.0, 1.0, 1.0]
        else:
            mutation_chances = [0.15, 0.15, 0.10]

        mutation_weights = {
            "Healthy": 30,
            "Meaty": 20,
            "Malnourished": 20,
            "tiny": 1,
            "GIANT": 1,
            "Radioactive": 0.2,
            "Void": 0.2,
            "Inky": 50,
            "Heavy": 40,
            "Burnt": 10,
            "Transparent": 2,
            "Gold": 15
        }

        available_mutations = [
            mutation for mutation in details["Mutation"]
            if mutation in mutation_weights
        ]

        caught_mutations = []

        # First mutation roll
        if random.random() < mutation_chances[0] and available_mutations:
            mutation = random.choices(
                available_mutations,
                weights=[mutation_weights[m] for m in available_mutations],
                k=1
            )[0]
            caught_mutations.append(mutation)
            available_mutations.remove(mutation)

        # Second mutation roll
        if random.random() < mutation_chances[1] and available_mutations:
            mutation = random.choices(
                available_mutations,
                weights=[mutation_weights[m] for m in available_mutations],
                k=1
            )[0]
            caught_mutations.append(mutation)
            available_mutations.remove(mutation)

        # Third mutation roll
        if random.random() < mutation_chances[2] and available_mutations:
            mutation = random.choices(
                available_mutations,
                weights=[mutation_weights[m] for m in available_mutations],
                k=1
            )[0]
            caught_mutations.append(mutation)
            available_mutations.remove(mutation)

        

        #-------------------FISH RESULT-------------------

        caught_fish = {
            "name": name,
            "rarity": fish_rarity,
            "mutation": ", ".join(caught_mutations) if caught_mutations else "None",
            "weight": fish_prices.fish_weight_generation(fish_rarity)
        }

        print(caught_fish)  # TEMPORARY

        for color in ("Color_1", "Color_2"):
            if color in details:
                caught_fish[color.upper()] = random.choice(details[color])

        return caught_fish


    def start(self): #Starts fishing
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

            self.cast_time_prompt = current_time + 100 #NOTE: FIXED TIME BEFORE CAST (Original: 1500)
            self.is_casting = "waiting"


        #2.5 Seconds before fishing starts

        elif self.is_casting == "waiting" and current_time >= self.cast_time_prompt:

            self.is_casting = False
            self.is_fishing = True
            self.start_time = current_time
            if self.debug_mode:
                self.duration = 0
            else:
             self.duration = random.uniform(2,4) #NOTE: THIS IS THE RANDOM TIME. ADJUST FOR DEBUG (Original: 2,4)



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












