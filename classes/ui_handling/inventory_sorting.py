
#SORTING ORDER:


CATEGORY_ORDER = {
    "FISH" : 0,
    "STONES" : 1,
    "SCRAP" : 2
}

RARITY_ORDER = {
    "SECRET" : 0,
    "APEX" : 1,
    "Endangered" : 2,
    "Legendary" : 3,
    "Epic" : 4,
    "Rare" : 5,
    "Common" : 6
}


def sort_inventory(items,sort_choice):

    if sort_choice == "Category":
        return sorted(
            items,
            key=lambda item: CATEGORY_ORDER.get(
                item.get("category" , "").upper(), 999
            )
        )

    elif sort_choice == "A-Z":
        return sorted(
            items,
            key=lambda item: item.get("name", "").casefold()
        )

    elif sort_choice == "Rarity":
        return sorted(
            items,
            key=lambda item: RARITY_ORDER.get(
                item.get("rarity"), 999
            )
        )

    elif sort_choice == "Weight":

        def get_weight(item):
            try:
                return -float(item["weight"])
            except (KeyError, TypeError, ValueError):
                return float("inf")
        return sorted(items, key = get_weight)
    return items


def swap_inventory_items(items, index_a, index_b):

    if(
        index_a < 0 or index_b < 0
        or index_a >= len(items) or index_b >= len(items)
        or index_a == index_b
    ):
        return False

    items[index_a], items[index_b] = items[index_b], items[index_a]
    return True