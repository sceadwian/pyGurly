import os
import csv
import random

def display_character_stats(character_name):
    # Load character stats from CSV file    
    with open(f"{character_name}.csv", "r") as character_file:
        character_reader = csv.reader(character_file)
        player_stats = next(character_reader)  # read only the first line of the file
    # Display character's stats in a table
    labels = ["Name", "Height", "Weight", "Size", "XP", "HP", "Stam", "Strg" , "Magk", "Agil","Intl", "Defc", "Jump", "Act1", "Act2", "Act3", "Act4", "Act5"]
    #recently added STRG make sure things are still working --> then added Intl
    #Name,Height,Weight,Size,XP,HP,Stam,Strg,Magk,Agil,Intl,Defc,Jump,Act1,Act2,Act3,Act4,Act5
    print(f"\n{'-'*28}")
    print(f"|{labels[0]:<12} | {player_stats[0]:>10} |")
    print(f"{'-'*28}")
    for label, stat in zip(labels[1:], player_stats[1:]):
        print(f"|{label:<12} | {stat:>10} |")
    print(f"{'-'*28}\n")
    return player_stats


def list_levels(): 
    # levels will be stored in CSV files
    # each file will be organized as follows:
    # level_name, level_loot_ID, boss_ID, mob1_ID, mob2_ID_mob3_ID, mob4_ID, mob5_ID, mob6_ID
    levels = []
    for file_name in os.listdir():
    # os.listdir() -> returns a list of all the files in the current directory
        if file_name.startswith("map_"):
            levels.append(file_name)
    # Display available levels
    print("Available levels:")
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")
    print()
    return levels

def load_level(levels):   
    # Ask user to select a level
    while True:
        try:
            level_choice = int(input("Select a level: "))
            if level_choice < 1 or level_choice > len(levels):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please try again.")
    level_chosen = levels[level_choice-1]
    return level_chosen



actions = [] # list of actions available to the player

#Here, we load the available actions from the player's CSV file and display them to the player. The player is then prompted to choose an action by entering the corresponding number, and the chosen action is used in the combat loop.

def combat_loop(player_stats, enemy_stats):
    actions_list = [
        #stam,strg,magk,agil,intl,defc,jump,heal,buff,Xstrg,Xmagk,Xagil,Xintl,Xdefc,Xjump,d-modifier
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],  # action 1 - Punch
        [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 10],  # action 2 - Kick
        [1, 0, 0, 0, 0, 0, 6, 1, 0, 0, 0, 0, 0, 0, 0, 10],  # action 3 - Block
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 4 - Recover
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 5 - Bash
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 6 - Rest Block
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 7 - Defensive Block
        [2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 8 - Roundhouse Kick
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 9 - Heal
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 10 - Magic Recovery
        [2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # action 11 - Levitate
        [2, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 12 - Floating Daggers
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 13 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 14 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 15 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 16 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 17 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 18 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 19 - 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # action 20 - 
    ]
    #initialize combat variables
    round_num = 1
    player_hp = int(player_stats["HP"])
    enemy_hp = int(enemy_stats["HP"])

    # ALL THE CSV loading was removed 20230430
    #load actions from player's CSV file -> player_stats[12:17] -> 


    # current idea is that we make damage/block based on adding components of 
    # strg + mgk + agl + int + def + jmp - Xstr - xmgk - xagil - xintl - xdef
    #combat loop
    while player_hp > 0 and enemy_hp > 0:
        print(f"\nRound {round_num}!")
        print(f"Player HP: {player_hp} | Enemy HP: {enemy_hp}\n")
        
        # display action options
        print("Choose an action:")
        for i, action in enumerate(player_actions):
            print(f"{i+1}. {action}")
        # prompt player for input
        while True:
            choice = input("Enter the number of the action you want to use: ")
            if choice.isdigit() and int(choice) in range(1, len(player_actions)+1):
                break
            else:
                print("Invalid input. Please enter the number of the action you want to use.")
        # use the chosen action
        player_action = player_actions[int(choice)-1]
        # calculate damage and defense
        player_dmg = int(player_stats["Stamina"]) * random.uniform(0.8, 1.2) # stamina * random multiplier
        enemy_def = int(enemy_stats["Defense"]) * random.uniform(0.8, 1.2) # defense * random multiplier
        enemy_dmg = int(enemy_stats["Stamina"]) * random.uniform(0.8, 1.2) - enemy_def # stamina * random multiplier - enemy defense
        if enemy_dmg < 0:
            enemy_dmg = 0
        # update HP
        player_hp -= enemy_dmg
        enemy_hp -= player_dmg
        # print round summary
        print(f"\nYou used {player_action} and dealt {int(player_dmg)} damage.")
        print(f"The enemy dealt {int(enemy_dmg)} damage.\n")
        round_num += 1
    
    #    fixed XP gain for winning - XP should be one of the values pulled from the csv file need to add that.
        #maybe i can use the same structure for mobs as the csv file for players, but instead of height and weight being there which
        #I intend to use to calculate size. instead that's where the, xp and loot info comes in... 
        # maybe petty mobs will drop crappy actions and bosses drop the good actions
    # determine winner and update stats
    if player_hp <= 0:
        print("You lost the battle.")
        update_character_stats(player_stats["Name"], 0, None) # update XP and action
        return "Enemy"
    else:
        print("You won the battle!")
        xp_gain = int(enemy_stats["XP"]) # XP gain for winning
        new_action = None # placeholder for action to be gained
        if round_num == 4: # boss fight
            xp_gain += 100 # extra XP for beating the boss
            new_action = "Super Move" # new action gained for beating the boss
        update_character_stats(player_stats["Name"], xp_gain, new_action) # update XP and action
        return "Player"







display_character_stats("Toon")
levels = list_levels()
chosen_level = load_level(levels)
print("Level chosen:", chosen_level)

