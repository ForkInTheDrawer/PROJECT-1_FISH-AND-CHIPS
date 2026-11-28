import json
import random

from pathlib import Path



class ShopStock:
    def __init__(self):

        project_root = Path(__file__).resolve().parents[3]
        gear_path = project_root / "data" / "gear_items.json"

        with gear_path.open(encoding = "utf-8") as file:
            self.item_data = json.load(file)

        self.gear_templates = self.item_data["GEAR"]
        self.consumable_templates = self.item_data["CONSUMABLES"]


    def generate_gear(self, category, item_name):
        category = category.upper()

        template = self.gear_templates[category][item_name]

        rolled_stats = {}

        for stat_name, stat_data in template.get("Stats", {}).items():

            if isinstance(stat_data, dict) and stat_data.get("Randomized"):

                value = random.uniform(
                    stat_data["Min"],
                    stat_data["Max"]
                )

                rolled_stats[stat_name] = round(value, 2)

            else:
                rolled_stats[stat_name] = stat_data

        return {
            "name": item_name,
            "category": category,
            "rarity": template.get("Rarity", "Common"),
            "description": template.get("Description", ""),
            "stats": rolled_stats,
            "price": template.get("Price", 0),
            "quantity": 1            
        }

    def generate_consumable(self, item_name):
        template = self.consumable_templates[item_name]

        return {
            "name" : item_name,
            "category": "CONSUMABLES",
            "rarity": template.get("Rarity", "Common"),
            "description": template.get("Description", ""),
            "stats": dict(template.get("Stats", {})),
            "amount": template.get("Amount", 1),
            "price": template.get("Price", 0),
            "quantity": 1            
         }

    def generate_stock(self):
        stock = []

        #Generate all gear Items.

        for category, items in self.gear_templates.items():
            for item_name in items:
                gear = self.generate_gear(category, item_name)
                stock.append(gear)

        #Generate all CONSUMABLE items:

        for item_name in self.consumable_templates:
            consumable = self.generate_consumable(item_name)
            stock.append(consumable)

        return stock