# Import the random library to use for the dice later
import random


# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion"]
    crafted_loot_options = ["Leather Armor", "Mystery Potion", "Glove of Secrets", "Healing Boots", "Encrypted Flask"]
    bad_loot_options = ["Poison Potion", "Toxic Gauntlet"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in crafted_loot_options:
        health_points = min(20, (health_points + 5))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
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
    total_monsters_killed = 0
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                if last_line.startswith("List of Monsters Killed:"):
                    total_monsters_killed = int(last_line.split(":")[1].strip())
    except FileNotFoundError:
        print("No previous save found. Creating a new save file.")
    if winner == "Hero":
        total_monsters_killed += 1
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously.\n")
        file.write(f"Total Monsters Killed: {total_monsters_killed}\n")


# Lab 06 - Question 5a
def load_game():
    total_monsters_killed = 0
    last_game = None
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_game = lines[-2].strip() if len(lines) > 1 else lines[-1].strip()
                last_line = lines[-1].strip()
                if last_line.startswith("Total Monsters Killed:"):
                    total_monsters_killed = int(last_line.split(":")[1].strip())
        print("    |    Loading from saved file ...")
        print(last_game)
        print(f"    |    Total Monsters Killed: {total_monsters_killed}")
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
    return last_game, total_monsters_killed


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
            print(
                "    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


# Term Project
def craft_items(belt):
    # Define crafting recipes (ALL possible combinations)
    crafting_recipes = {
        frozenset(["Leather Boots", "Flimsy Gloves"]): "Leather Armor",
        frozenset(["Health Potion", "Poison Potion"]): "Mystery Potion",
        frozenset(["Secret Note", "Flimsy Gloves"]): "Glove of Secrets",
        frozenset(["Poison Potion", "Flimsy Gloves"]): "Toxic Gauntlet",
        frozenset(["Health Potion", "Leather Boots"]): "Healing Boots",
        frozenset(["Secret Note", "Health Potion"]): "Encrypted Flask",
    }

    crafted = True
    while crafted:
        crafted = False
        for ingredients, result in crafting_recipes.items():
            if all(belt.count(item) >= list(ingredients).count(item) for item in ingredients):
                for item in ingredients:
                    belt.remove(item)
                belt.append(result)
                print(f"Crafted {result} from {list(ingredients)}!")
                crafted = True
                break  # Restart after crafting to avoid overlap

    return belt