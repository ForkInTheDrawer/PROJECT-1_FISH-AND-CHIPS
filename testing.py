#NOTE: Test stuff here.


from classes.ui_handling.sales.shop_stock import ShopStock


shop = ShopStock()


print( " \n ===GEAR TEST===")


gear = shop.generate_gear("HEAD", "Bucket Hat")
print(gear)


print("\n CONSUMABLE TEST")

consumable = shop.generate_consumable("Basic Bait")
print(consumable)


print("\n=== Checking===")

print(f"Gear Category: {gear['category']}")
print(f"Gear rolled stats: {gear['stats']}")

print(f"Consumable amount: {consumable['amount']}")
print(f"Consumable quantity: {consumable['quantity']}")
print(f"Consumable stats: {consumable['stats']}")