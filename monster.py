from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        
    def monster_attacks(self, hero):
        print("Monster attacks the hero!")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print(f"The monster has reduced Player's health to: {hero.health_points}")
    
    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
