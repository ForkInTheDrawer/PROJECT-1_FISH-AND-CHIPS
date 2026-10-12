class character:
    def __init__(self, name_val, gender_val, cash_val, chips_val, luck_val):
        self.name = name_val
        self.gender = gender_val
        self.cash = cash_val
        self.chips = chips_val
        self.luckMult = luck_val



        #NOTE: DO THESE LATER ONCE YOU UNDERSTAND HOW TO IMPLEMENT THEM:
        # self.gender = gender
        # self.cash = cash
        # self.chips = chips
        # self.luck = luck
    def get_money(self, name):
        
        print(f"{self.name}")
        
person_a = character("Ivan", "M", 100, 0, 1)
person_b = character("John", "M", 92, 0, 1)