# PROJECT-1-FISH-AND-CHIPS

PROJECT IDEAS:
APP:

Fish n Chips
FISHING GAME (Inspired by gimkit's Fishing game)

-Cast your rod, wait for it to catch a fish.
-Sell raw fishes to gain Coins
-Sell Cooked Fishes to gain CHIPS
-Use the coins to upgrade your rod
-Use CHIPS to buy 

-NOTE: Upgrades are as follows:
-Rod material (+ durability & Weight)
-Line Material (+Weight)
-Bait / Hook (++Luck)
-Reel (+Speed)
-Handle (+Durability)


CHIPS

Chips = Special currency to buy a buff w/ a debuff in the "BLACK MARKET"


## Development Progress

### Current task: Fishing interaction

- [x] Add a proximity detector import and create a fishing proximity detector after the `dock` rectangle is defined in `main.py`.
- [ ] Replace the contents of `classes/proximity_detector.py` with the proximity detector implementation discussed in the development chat.
- [ ] Connect the detector to the game loop so pressing **E** near the dock triggers the fishing interaction.
- [ ] Show a prompt such as **Press E to fish** when the player is close enough to the dock.

### Next steps

1. Finish and save `classes/proximity_detector.py`.
2. Connect the detector to the keyboard event handling in `main.py`.
3. Test the interaction in-game and fix any issues before adding more features.

> Progress note: The proximity detector file replacement has not yet been confirmed complete. Update this checklist as each step is finished.
