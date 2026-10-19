import random
import pygame


class Fishing:
    # adds up to 100%.
    TYPE_WEIGHTS = {
        "Common": 60,
        "Rare": 20,
        "Epic": 10.5,
        "Legendary": 8,
        "Endangered": 1,
        "APEX": 0.5,
    }

    
    MUTATION_WEIGHTS = {
        "Healthy": 30,
        "Meaty": 12,
        "Malnourished": 12,
        "Colorful": 10,
        "tiny": 5,
        "GIANT": 5,
        "Radioactive": 0.5,
        "Red": 50,
        "Inky": 50,
        "Heavy": 40,
        "Burnt": 10,
        "Transparent": 2,
        "Gold": 15,
    }

    MUTATION_ROLL_CHANCES = (0.10, 0.10, 0.10)

    def __init__(self, fish_data):
        self.fish_data = fish_data

        self.is_fishing = False
        self.is_casting = False
        self.start_time = 0
        self.duration = 0
        self.cast_time_prompt = 0

    def choose_fish(self):
        # Ignore any unfinished fish entries without Type or Mutation lists.
        available_fish = {
            name: details
            for name, details in self.fish_data.items()
            if details.get("Type") and details.get("Mutation")
        }
        if not available_fish:
            raise ValueError("No fish have valid Type and Mutation lists in fishies.json.")

        name = random.choice(list(available_fish))
        details = available_fish[name]

        # Only use type options that have a configured weight.
        type_options = [
            fish_type for fish_type in details["Type"]
            if fish_type in self.TYPE_WEIGHTS
        ]
        if not type_options:
            raise ValueError(f"No configured type weights for fish: {name}")

        caught_type = random.choices(
            type_options,
            weights=[self.TYPE_WEIGHTS[fish_type] for fish_type in type_options],
            k=1,
        )[0]

        # Keep only one copy of each available mutation.
        remaining_mutations = list(dict.fromkeys(details["Mutation"]))
        applied_mutations = []

        # A roll is attempted only if the previous mutation roll succeeded.
        # Each successful roll chooses one mutation by relative weight.
        for chance in self.MUTATION_ROLL_CHANCES:
            if not remaining_mutations or random.random() >= chance:
                break

            mutation = random.choices(
                remaining_mutations,
                weights=[
                    self.MUTATION_WEIGHTS.get(name, 1)
                    for name in remaining_mutations
                ],
                k=1,
            )[0]
            applied_mutations.append(mutation)
            remaining_mutations.remove(mutation)

        caught_fish = {
            "name": name,
            "type": caught_type,
            "mutations": applied_mutations,
        }

        # Preserve optional fish color data, if present.
        for color in ("Color_1", "Color_2"):
            if color in details and details[color]:
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

        # Wait 0.2 seconds before showing the casting message.
        if self.is_casting is True and current_time >= self.cast_time_prompt:
            print("Casting Bait...")
            self.cast_time_prompt = current_time + 1500
            self.is_casting = "waiting"

        # Wait 1.5 seconds before fishing starts.
        elif self.is_casting == "waiting" and current_time >= self.cast_time_prompt:
            self.is_casting = False
            self.is_fishing = True
            self.start_time = current_time
            self.duration = random.uniform(2, 4)

            print(
                "Fishing Started! Catch Time:",
                round(self.duration, 1),
                "seconds.",
            )

        # Check whether a fish has been caught.
        elif self.is_fishing:
            elapsed_time = (current_time - self.start_time) / 1000

            if elapsed_time >= self.duration:
                self.is_fishing = False
                return True

        return False


# NOTE: This is for fish rarity/price/weight data.
class fish_rarity:
    def __init__(self, rarity, price, weight):
        self.rarity = rarity
        self.price = price
        self.weight = weight
