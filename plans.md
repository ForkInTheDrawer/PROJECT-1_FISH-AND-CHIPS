# PROJECT IDEAS:

## IMPORTANT:
WHEN SAVING YOUR PROJECT TO GITHUB:
* DO THESE STEPS:
1. Save file (via Ctrl + S)
2. Go to Source Control (3rd icon on the left)
3. Press "+" Button (named "Stage Changes")
4. Add a Message (NOTE: PUT THE CHANGES U ADDED.)
5. Press Commit
6. Click the "push" icon on the graph.

7. NOTE: If importing these changes from GitHub, type these in the terminal:
* `git status`
* `git pull`

-------------------------
START HERE:


# Development Progress

### Finished task: 
- Movement
- Fishing interaction
-  RNG Fishing System
- Selling Mechanic
- UI (for Cash)

### Work In Progress:

(UI Focused)
- Work on GUI:
    * "Press Q to Sell" GUI near Vendor
    * "Press F to Open SHop" GUI near Fishing Shop

 (Focused on the fishing system)
- Add a way so that Scrap items can be caught and sold.
    * Add a mutation
    * Make it so it can be sold
- Add more Fishes (?)
- Different Fish Chances (RNG)
    * Some fishes are rarer than the other.
    * Rarity for certain fishes are Epic +, or smth like that.
    * Common Fishes get Common - Epic Rarity.
    * Rare Fishes get Epic - Endangered Rarity
    * Super Rare Fishes get Epic - SECRET Rarity.



### Future Task:

- Inventory Icon + Inventory Mechanic
    * "Lock Item" Mechanic - To stop it from getting sold.

- Fishing Minigame (During Casting Bait sequence)

- Add Animation:
    * "Press E To Fish" Popup
    * Fish Results Popup Screen Effect
    * Sell UI Animation 



- Stats on Basic Rod
    * Make a new .py file named "rods"
        * Stats:
            - Weight (Higher Weight chance)
            - Durability (Higher Weight chance)
            - Luck (Better Fish Chance)
            - Speed (Faster fishing and Casting time)




- Shops and Fishing Upgrades:
    * Shop System
        * Put 3 Testing Fishing Rods + Backpack
        * Timely Rotation (Can skip rotation using money)
    

    * Rod Upgrades: 
        - Rod material (+ durability & Weight)
        - Line Material (+Weight)
        - Bait / Hook (++Luck)
        - Reel (+Speed)
        - Handle (+Durability)



NTS:
# Fish n Chips

- Cast your rod, wait for it to catch a fish.
- Sell raw fish to gain Coins.
- Sell cooked fish to gain CHIPS.
- Use Coins to upgrade your rod.
- Use CHIPS to buy special buffs with debuffs in the BLACK MARKET.

## Upgrades
- Rod material: durability and weight capacity
- Line material: weight tolerance + line distance
- Bait / hook: luck + bigger bait, bigger fish
- Reel: reeling speed
- Handle: Luck




### PLANS:
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

















---

# Sprite implementation roadmap (beginner-friendly)

**Goal:** Replace the temporary red rectangle with an image, then build up to animated sprites without breaking movement or the camera. Finish one stage and test it before moving on.

## Stage 1 — Prepare one image
- [ ] Create an `assets/sprites/` folder in the project.
- [ ] Put one player image in it, for example `player.png`.
- [ ] Prefer a PNG with a transparent background.
- [ ] Keep the image small and simple for the first test; do not start with a full animation sheet yet.

**Learn:** An image file is an asset. Pygame loads it into a `Surface`, which is an image that can be drawn on the screen.

**Checkpoint:** You can find the image file in your project and know its path.

## Stage 2 — Load and draw the image
- [ ] In `main.py`, load the image after `pygame.init()` (and after creating the display is a good place).
- [ ] Use `pygame.image.load(...).convert_alpha()` for a PNG that needs transparency.
- [ ] Temporarily draw the loaded image with `screen.blit(player_image, (x, y))`.
- [ ] Comment out the red rectangle while testing so you can clearly see the image.

**Learn:** `pygame.image.load()` loads the file; `convert_alpha()` preserves per-pixel transparency; `blit()` draws a Surface onto another Surface.

**Checkpoint:** The image appears on the screen. If it does not, check the file path and the error message before changing movement code.

## Stage 3 — Give the image a useful size and position
- [ ] Check the image's natural size.
- [ ] If needed, resize it with `pygame.transform.scale()` or `pygame.transform.smoothscale()`.
- [ ] Use the image's rectangle (`player_image.get_rect()`) to position it.
- [ ] Keep a clear distinction between the player's world position and where the player is drawn on screen.

**Learn:** The image is visual; a `pygame.Rect` is useful for position and collision bounds. They can share dimensions, but they are not the same thing.

**Checkpoint:** The sprite is a sensible size and appears where the red rectangle used to be.

## Stage 4 — Connect the sprite to movement and the camera
- [ ] Keep using the existing movement input and speed logic at first.
- [ ] Update the player's world position, then calculate the camera offset.
- [ ] Draw the island and the sprite using the same camera offset.
- [ ] Keep the player drawn at the screen center if that is the camera style you want.
- [ ] Keep island-boundary checks in world coordinates, not screen coordinates.

**Learn:** The camera changes drawing positions; it should not change the player's actual world position. Every world object should use the same camera offset when it is drawn.

**Checkpoint:** The sprite stays centered while the island moves, and the player still cannot leave the island.

## Stage 5 — Create a Player class for the game character
- [ ] Once the image works in `main.py`, move the player-specific data into a dedicated class (for example, in `player.py`).
- [ ] Give it an image, a world position, a rectangle, and a movement/update method.
- [ ] Let `main.py` handle the game loop and call the player's methods.
- [ ] Keep the existing `character.py` stats class separate for now, or rename classes later so the purpose of each class is clear.

**Learn:** A class groups the data and behavior that belong to one game object. Refactor only after the simple version works.

**Checkpoint:** The game still behaves the same after the player logic is moved into its class.

## Stage 6 — Add a simple walking animation
- [ ] Prepare 2–4 images of the same character, or a sprite sheet with frames.
- [ ] Load the frames and switch between them while the player moves.
- [ ] Use elapsed time to control animation speed; do not change frames every loop iteration without timing.
- [ ] Use one frame when the player is idle.

**Learn:** Animation is a sequence of images displayed over time. Movement speed and animation speed are separate things.

**Checkpoint:** The character animates while moving and returns to an idle image when standing still.

## Stage 7 — Add other sprites
- [ ] Add one object at a time, such as a tree, rock, fishing spot, or fish.
- [ ] Store world positions for objects that belong to the map.
- [ ] Apply the same camera offset when drawing them.
- [ ] Once there are several objects, learn `pygame.sprite.Sprite` and `pygame.sprite.Group` to organize and draw them.

**Learn:** A sprite group helps manage many objects; it is useful, but you do not need it just to display your first player image.

**Checkpoint:** Multiple objects render in the correct world positions while the camera moves.

## Stage 8 — Add collisions and fishing interactions
- [X] Decide which objects need collision rectangles.
- [X] Test simple collisions with `Rect` overlap checks.
- [X] Add interaction logic for fishing spots or fish only after movement, drawing, and camera behavior are reliable.

**Checkpoint:** The player can approach an object and trigger a simple interaction without the camera breaking.



## Sprite rules to remember
- Load assets once, not every frame inside the main loop.
- Draw with `blit()`; use `pygame.draw.rect()` only for debug shapes or objects that are intentionally simple.
- Update game/world positions first, then draw.
- Apply the camera offset consistently to every world object.
- Keep the first milestone tiny: one static player image before animation, sprite groups, or collisions.
- `import sys` is not needed for loading or drawing sprites. Keep it only if you later use something from `sys`; it does not affect the sprite workflow.
