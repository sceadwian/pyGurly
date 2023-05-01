import os
import csv
import random

def display_character_stats(character_name):
    # Load character stats from CSV file    
    with open(f"{character_name}.csv", "r") as character_file:
        character_reader = csv.reader(character_file)
        player_stats = next(character_reader)  # read only the first line of the file
    # Convert numerical stats to integers
    player_stats = [player_stats[0]] + [int(stat) for stat in player_stats[1:]]
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
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 6],  # action 1 - Punch
        [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 10],  # action 2 - Kick
        [1, 0, 0, 0, 0, 0, 6, 1, 0, 0, 1, 0, 0, 1, 0, 10],  # action 3 - Block
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 6],  # action 4 - Recover
        [2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 6],  # action 5 - Bash
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 6],  # action 6 - Rest Block
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 6],  # action 7 - Defensive Block
        [2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 10],  # action 8 - Roundhouse Kick
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 6],  # action 9 - Heal
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 6],  # action 10 - Magic Recovery
        [2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 6],  # action 11 - Levitate
        [2, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 6],  # action 12 - Floating Daggers
        [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 6],  # action 13 - Gaseous Punishment
        [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 10],  # action 14 - Copper Sword
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 10],  # action 15 - Nunchucks
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 6],  # action 16 - Copper Axe
        [2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 0, 10],  # action 17 - Simple Hammer
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6],  # action 18 - Monster1
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 10],  # action 19 - Monster2
        [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 6],  # action 20 - Monster3
    ]
   
    #initialize combat variables
    round_num = 1
    player_hp = int(player_stats[5])
    enemy_hp = int(enemy_stats[5])

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
        for i, action in enumerate(player_stats[13:18]):
            print(f"{i+1}. {action}")
        # prompt player for input
        while True:
            choice = input("Enter the number of the action you want to use: ")
            if choice.isdigit() and int(choice) in range(1, len(player_stats[13:18])+1): 
                  break
            else:
                print("Invalid input. Please enter the number of the action you want to use.")
        # use the chosen action
        player_action = actions_list[int(choice)-1]

        player_dmg = (int(player_stats[6])
                      + int(player_stats[7]) * player_action[int(choice)-1]["modifiers"][0]
                      + int(player_stats[8]) * player_action[int(choice)-1]["modifiers"][1]
                      + int(player_stats[9]) * player_action[int(choice)-1]["modifiers"][2]
                      + int(player_stats[10]) * player_action[int(choice)-1]["modifiers"][3]
                      + int(player_stats[11]) * player_action[int(choice)-1]["modifiers"][4]
                      + int(player_stats[12]) * player_action[int(choice)-1]["modifiers"][5])
        enemy_dmg = (int(enemy_stats[7]) * player_action[int(choice)-1]["modifiers"][6]
                     + int(enemy_stats[8]) * player_action[int(choice)-1]["modifiers"][7]
                     + int(enemy_stats[9]) * player_action[int(choice)-1]["modifiers"][8]
                     + int(enemy_stats[10]) * player_action[int(choice)-1]["modifiers"][9]
                     + int(enemy_stats[11]) * player_action[int(choice)-1]["modifiers"][10]
                     + int(enemy_stats[12]) * player_action[int(choice)-1]["modifiers"][11])

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
    

#        if enemy_dmg < 0:
#            enemy_dmg = 0
#
#        player_hp -= enemy_dmg
#        enemy_hp -= player_dmg
#        print(f"\nYou used {player_action} and dealt ", end="")
#        if int(player_dmg) > 10:
#            print(f"\033[32m{int(player_dmg)}\033[0m", end="")
#        elif int(player_dmg) > 0:
#            print(f"\033[33m{int(player_dmg)}\033[0m", end="")
#        else:
#            print("0", end="")
#        print(" damage.")
#        print(f"The enemy dealt ", end="")
#        if int(enemy_dmg) > 10:
#            print(f"\033[32m{int(enemy_dmg)}\033[0m", end="")
#        elif int(enemy_dmg) > 0:
#            print(f"\033[33m{int(enemy_dmg)}\033[0m", end="")
#        else:
#            print("0", end="")
#        print(" damage.\n")
#        round_num += 1
#    if player_hp <= 0:
#        print("You lost the battle.")
#        update_character_stats(player_stats["Name"], 0, None)
#        return "Enemy"

    else:
        print("You won the battle!")
        xp_gain = int(enemy_stats["XP"]) # XP gain for winning
        new_action = None # placeholder for action to be gained
        if round_num == 4: # boss fight
            xp_gain += 100 # extra XP for beating the boss
            new_action = "Super Move" # new action gained for beating the boss
        update_character_stats(player_stats["Name"], xp_gain, new_action) # update XP and action
        return "Player"





player_stats = display_character_stats("Toon")

# print all values of player_stats here
print(player_stats)

levels = list_levels()
chosen_level = load_level(levels)
print("Level chosen:", chosen_level)
combat_start = combat_loop(player_stats, player_stats)


