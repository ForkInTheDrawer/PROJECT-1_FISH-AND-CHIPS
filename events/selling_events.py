from classes.fishing import fish_prices
from classes.ui_handling import gui
from classes.fishing.scrap_mutations import SCRAP_MUTATIONS
from classes.ui_handling.sales.sell_confirmation import Sell_Confirmation


# FOR SELLING
def calculate_stone_price(stone, item_index):

    tier_multipliers = {
        "Honed" : 1.0,
        "Tidebound" : 2.5,
        "Soulbound" : 3.0,
        "Aetherbound" : 5.0
    }

    base_price = stone["base_price"]
    rarity = stone["rarity"]
    multiplier = tier_multipliers.get(rarity, 1.0)

    sale_price = base_price * multiplier

    return sale_price

#STONE
def cancel_sell_stone(player_data, item_index):
    items = player_data.inventory["plr_inv"]

    if not 0 <= item_index < len(items):
        return

    stone = items.pop(item_index)
    items.append(stone)

    player_data.save_inventory()

    print(f"Moved {stone['name']} to the back of inventory.")


def accept_sell_stone(player_data, item_index):
    items = player_data.inventory["plr_inv"]

    if not 0 <= item_index < len(items):
        return None

    stone = items[item_index]

    if stone.get("category") != "STONES":
        return None

    sale_price = round(calculate_stone_price(stone, item_index))
    items.pop(item_index)

    player_data.chips += sale_price

    print(f"Chips: {player_data.chips:.2f}")
    player_data.save_inventory()

    return{
        "name" : stone["name"],
        "price" : sale_price,
        "currency" : "Chips"
    }


#OTHER THINGS
def sell_regular_item(player_data, item, item_index):
    items = player_data.inventory["plr_inv"]
    if not 0 <= item_index < len(items):
        return None

    if items[item_index] is not item:
        return None


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
        sale_price = round(sale_price)
        items.pop(item_index)

        if currency == "Chips":
            player_data.chips += sale_price

        else:
            player_data.cash += sale_price

        player_data.save_inventory()

        return{
            "name" : item["name"],
            "price" : sale_price,
            "currency" : currency.title()
        }

def open_sell_confirmation(item):
    print("Rare Material Detected.")
    return Sell_Confirmation(item["name"])



def sell_all_unlocked(player_data):
    items = player_data.inventory["plr_inv"]

    total_coins = 0
    total_chips = 0
    sold_count = 0
    remaining_items = []

    for item in items:
        if item.get("locked", False):
            remaining_items.append(item)
            continue

        category = item.get("category")

        if category == "STONES":
            sale_price = round(calculate_stone_price(item, None))
            total_chips += sale_price

        elif category == "SCRAP":
            mutation = item.get("mutation")

            if mutation=="Glitched":
                sale_price = round(item["price"])
                total_chips += sale_price

            else:
                mutation_data = SCRAP_MUTATIONS.get(mutation)
                multiplier = (
                    mutation_data["multiplier"]
                    if mutation_data else 1.0
                )
                sale_price = round(item["price"] * multiplier)
                total_coins += sale_price
        else:
            sale_price = fish_prices.price_calculator(item)

            if sale_price is None:
                remaining_items.append(item)
                continue

            sale_price = round(sale_price)
            total_coins += sale_price
        sold_count += 1
    if sold_count > 0:
        player_data.inventory["plr_inv"] = remaining_items

        player_data.cash += total_coins
        player_data.chips += total_chips

        player_data.save_inventory()

    return{
        "count" : sold_count,
        "coins" : total_coins,
        "chips" : total_chips
    }


def calculate_unlocked_val(player_data):
    items = player_data.inventory["plr_inv"]

    total_coins = 0
    total_chips = 0
    item_count = 0

    for item in items:
        if item.get("locked", False):
            continue

        category = item.get("category")

        if category == "STONES":
            sale_price = round(calculate_stone_price(item, None))
            total_chips += sale_price

        elif category =="SCRAP":
            mutation = item.get("mutation")

            if mutation == "Glitched":
                sale_price = round(item["price"])
                total_chips += sale_price
            else:
                mutation_data = SCRAP_MUTATIONS.get(mutation)
                multiplier = (
                    mutation_data["multiplier"]
                    if mutation_data else 1.0
                )
                sale_price = round(item["price"] * multiplier)
                total_coins += sale_price
        else:
            sale_price = fish_prices.price_calculator(item)

            if sale_price is None:
                continue

            sale_price = round(sale_price)
            total_coins += sale_price

        item_count += 1

    return {
        "count" : item_count,
        "coins" : total_coins,
        "chips" : total_chips
    }