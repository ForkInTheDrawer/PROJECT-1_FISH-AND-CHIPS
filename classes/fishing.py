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


    #--------------------------RARITIES--------------
        type_names = [
            "Common",
            "Rare",
            "Epic",
            "Legendary",
            "Endangered",
            "APEX",
            "SECRET"
        ]
        type_weights = [60, 20, 10.5, 8, 0.999, 0.5, 0.001]
        fish_type = random.choices(
            type_names,
            weights=type_weights,
            k=1
        )[0]


        mutation_weights = {
            "Healthy":30,
            "Meaty": 20,
            "Malnourished": 20,
            "Colorful": 10,
            "tiny": 5,
            "GIANT":5,
            "Radioactive": 0.5,
            "Void" : 0.5,
            "Inky":50,
            "Heavy" :40,
            "Burnt":10,
            "Transparent": 2,
            "Gold":15
        }


        available_mutations = [
            mutation for mutation in details["Mutation"]
            if mutation in mutation_weights
        ]

        caught_mutations = []

        #FIRST MUTATION = CURRENTLY 100%, DEBUG MODE (Original = 15%)

        if random.random() < 1 and available_mutations: 
            mutation = random.choices(
                available_mutations,
                weights = [mutation_weights[m] for m in available_mutations],
                k = 1
            )[0]
            caught_mutations.append(mutation)
            available_mutations = [
                m for m in available_mutations
                if m != mutation
            ]

            #NOTE: WORK ON SECOND MUTATION ROLL CHANCE!!!
        
        #SECOND MUTATION = CURRENTLY 100%, DEBUG MODE. (Original = 15%)

            if random.random() < 1 and available_mutations: 
                mutation = random.choices(
                    available_mutations,
                    weights = [mutation_weights[m] for m in available_mutations],
                    k=1
                )[0]
                caught_mutations.append(mutation)
                available_mutations =[
                    m for m in available_mutations
                    if m != mutation
                ]


                #THIRD MUTATION = CURRENTLY 100%, DEBUG MODE. (Original = 10%)

                if random.random() <1 and available_mutations:
                    mutation = random.choices(
                        available_mutations,
                        weights = [mutation_weights[m] for m in available_mutations],
                        k = 1
                    )[0]
                    caught_mutations.append(mutation)
                    available_mutations = [
                        m for m in available_mutations
                        if m != mutation
                    ]



    #-------------------RNG SYSTEM
        caught_fish = {
            "name": name,
            "type": fish_type,
            "mutation": ", ".join(caught_mutations) if caught_mutations else "None"
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

            self.cast_time_prompt = current_time + 100 #NOTE: FIXED TIME BEFORE CAST (Original: 1500)
            self.is_casting = "waiting"


        #2.5 Seconds before fishing starts

        elif self.is_casting == "waiting" and current_time >= self.cast_time_prompt:

            self.is_casting = False
            self.is_fishing = True
            self.start_time = current_time
            self.duration = random.uniform(0,1) #NOTE: THIS IS THE RANDOM TIME. ADJUST FOR DEBUG (Original: 2,4)

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


