from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()    
    def hero_attacks(self, monster):
        print("Hero attacks the monster!")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("You have killed the monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"You reduced the monster's health to: {monster.health_points}")
    
    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
