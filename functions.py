# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")
# it wont print because its commented out. 

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly check your first item:")
    if belt:
        # Peek at the first item without removing it
        first_item = belt[0]
        if first_item in ["Dragon Scale", "Phoenix Feather", "Unicorn Horn"]:
            print("    |    You decide to save the " + first_item + " for casting spells.")
        else:
            # Remove the item and apply its effect
            first_item = belt.pop(0)
            if first_item in good_loot_options:
                health_points = min(20, (health_points + 2))
                print("    |    You used " + first_item + " to up your health to " + str(health_points))
            elif first_item in bad_loot_options:
                health_points = max(0, (health_points - 2))
                print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
            else:
                print("    |    You used " + first_item + " but it's not helpful")
    else:
        print("    |    Your belt is empty!")
    return belt, health_points



def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

# Lab 06 - Question 5a
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")

def cast_spell(belt, monster_health, hero_health):
    """
    Battle Spells feature: Uses items in the hero's belt to cast spells.
    
    Spells:
      - If the belt contains both "Dragon Scale" and "Phoenix Feather": cast "Flame Shield" (bonus damage: 3).
      - If the belt contains "Dragon Scale" but not "Phoenix Feather": cast "Dragon's Might" (bonus damage: 2).
      - If neither of the above but the belt contains "Unicorn Horn": cast "Healing Light" (heal hero by 3).
      - Otherwise, no spell is cast.
      
    Items used for the spell are removed from the belt.
    """
    
    print("    |     Current belt:", belt)
    
    spell = "No Spell"
    bonus_damage = 0
    heal_amount = 0

   
    if "Dragon Scale" in belt:
        if "Phoenix Feather" in belt:
            spell = "Flame Shield"
            bonus_damage = 3
            print("    |     Found Dragon Scale and Phoenix Feather.")
            belt.remove("Dragon Scale")
            belt.remove("Phoenix Feather")
        else:
            spell = "Dragon's Might"
            bonus_damage = 2
            print("    |     Found Dragon Scale without Phoenix Feather.")
            belt.remove("Dragon Scale")
    elif "Unicorn Horn" in belt:
        spell = "Healing Light"
        heal_amount = 3
        print("    |     Found Unicorn Horn.")
        belt.remove("Unicorn Horn")
    else:
        print("    |    No applicable magical items found.")
    
    if spell in ["Flame Shield", "Dragon's Might"]:
        print(f"    |    Casting {spell}! It deals an extra {bonus_damage} damage to the monster!")
        monster_health = max(0, monster_health - bonus_damage)
    elif spell == "Healing Light":
        print(f"    |    Casting {spell}! It heals the hero by {heal_amount} points!")
        hero_health = min(20, hero_health + heal_amount)
    else:
        print("    |    No magical items available to cast a spell.")
    
    
    print("    |     Updated belt:", belt)
    print("    |  Monster health:", monster_health, "Hero health:", hero_health)
    
    return belt, monster_health, hero_health

