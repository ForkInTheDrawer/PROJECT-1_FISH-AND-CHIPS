from classes.fishing import fish_prices
from classes.ui_handling import gui
from classes.fishing.scrap_mutations import SCRAP_MUTATIONS



# FOR SELLING
def calculate_stone_price(stone):

    tier_multipliers = {
        "Honed" : 1.0,
        "Tidebound" : 2.5,
        "Soulbond" : 3.0,
        "Aetherbound" : 5.0
    }

    base_price = stone["base_price"]
    rarity = stone["rarity"]
    multiplier = tier_multipliers.get(rarity, 1.0)

    sale_price = base_price * multiplier

    return sale_price

#STONE
def cancel_sell_stone(player_data):
    stone = player_data.inventory["plr_inv"].pop(0)

    player_data.inventory["plr_inv"].append(stone)
    player_data.save_inventory()


    print(f"Moved {stone['name']} to the back of inventory.")


def accept_sell_stone(player_data):
    stone = player_data.inventory["plr_inv"][0]

    sale_price = calculate_stone_price(stone)

    player_data.inventory["plr_inv"].pop(0)
    player_data.chips += sale_price
    print(f"Chips: {player_data.chips:.2f}")

    player_data.save_inventory()

    print(f"Sold {stone['name']} for {sale_price:.2f} Chips.")


#OTHER THINGS
def sell_regular_item(player_data, item):

    if item.get("category") == "SCRAP":
        mutation = item.get("mutation")

        if mutation == "Glitched":
            sale_price = item["price"]
            currency = "Chips"

        else:
            mutation_data = SCRAP_MUTATIONS.get(mutation)
            multiplier = mutation_data["multiplier"] if mutation_data else 1.0
            sale_price = item["price"] * multiplier
            currency = "coins"

    else:
        sale_price =fish_prices.price_calculator(item)
        currency = "Coins"

    if sale_price is not None:
        player_data.inventory["plr_inv"].pop(0)

        if currency == "Chips":
            player_data.chips += sale_price
        else:
            player_data.cash += sale_price

        player_data.save_inventory()

        print(f"Sold {item['name']} for {sale_price:.2f} {currency}.")

def open_sell_confirmation(item):
    print("Rare Material Detected.")
    return gui.Sell_Confirmation(item["name"])