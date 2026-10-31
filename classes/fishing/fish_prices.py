import random

FISH_WEIGHT_RANGES={
    "Common": (1.0 , 3.0),
    "Rare": (2.0,8.0),
    "Epic": (5.0 , 20.0),
    "Legendary": (15.0 , 50.0),
    "Endangered":(25.0, 100.0),
    "APEX": (50.0 , 200.0),
    "SECRET": (100.0, 500.0)
}




def fish_weight_generation(fish_rarity):
    min_weight, max_weight = FISH_WEIGHT_RANGES.get(
        fish_rarity,
        (1.0, 30)
    )

    return round(random.uniform(min_weight , max_weight), 1)


#NOTE: BASE STUFFS.
RARITY_PRICE = {
    "Common": 5,
    "Rare" : 10,
    "Epic" : 45,
    "Legendary": 100,
    "Endangered": 250,
    "APEX" : 600,
    "SECRET" : 2500

}

MUTATION_MULTIPLIER = {
    "Malnourished" : 0.7,
    "tiny" : 0.9 ,
    "Burnt": 0.9,
    "Healthy" : 1.1,
    "Inky" : 1.1 ,
    "Meaty" : 1.25,
    "Heavy" : 1.32,
    "Transparent": 1.5,
    "GIANT": 1.5,
    "Gold": 2.0,
    "Radioactive": 2.25,
    "Void": 3.0,

}


def price_calculator(fish):
    base_price = RARITY_PRICE.get(fish["rarity"], 5)

    mutations = fish["mutation"].split(",")
    mutation_multiplier = 1.0

    for mutation in mutations:
        if mutation != "None":
            mutation_multiplier *= MUTATION_MULTIPLIER.get(
                mutation, 1.0
            )

    weight_multiplier = fish.get("weight" , 1.0)

    return base_price * weight_multiplier * mutation_multiplier


#NOTE: FOR TESTING
# test_fish = {
#     "name" : "Test Fish",
#     "rarity" : "SECRET",
#     "mutation" : "Void", 
#     "weight" : 20.0,
# }

# print ('Result:' , " ", price_calculator(test_fish) )










#PLACEHOLDER
class fish_rarity():
    def __init__ (self, rarity, price, weight):
        self.rarity = rarity
        self.price = price
        self.weight = weight


    

        #Placeholder for fish types