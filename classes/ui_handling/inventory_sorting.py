
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


def sort_inventory_indices(items, sort_choice):
    """Return display positions without changing the saved inventory list."""
    indices = list(range(len(items)))

    if sort_choice == "Default":
        return indices

    if sort_choice == "Category":
        return sorted(
            indices,
            key=lambda index: CATEGORY_ORDER.get(
                items[index].get("category", "").upper(), 999
            )
        )

    if sort_choice == "A-Z":
        return sorted(
            indices,
            key=lambda index: items[index].get("name", "").casefold()
        )

    if sort_choice == "Rarity":
        return sorted(
            indices,
            key=lambda index: RARITY_ORDER.get(
                items[index].get("rarity"), 999
            )
        )

    if sort_choice == "Weight":
        def get_weight(index):
            try:
                return -float(items[index]["weight"])
            except (KeyError, TypeError, ValueError):
                return float("inf")
        return sorted(indices, key=get_weight)

    return indices