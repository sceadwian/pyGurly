import os
import csv
import random

def display_character_stats(character_name):
    # Load character stats from CSV file    
    with open(f"{character_name}.csv", "r") as character_file:
        character_reader = csv.reader(character_file)
        character_stats = next(character_reader)  # read only the first line of the file
    # Display character's stats in a table
    labels = ["Name", "Height", "Weight", "Size", "XP", "HP", "Stam", "Strg" , "Magk", "Agil", "Defc", "Jump"]
    #recently added STRG make sure things are still working
    print(f"\n{'-'*28}")
    print(f"|{labels[0]:<12} | {character_stats[0]:>10} |")
    print(f"{'-'*28}")
    for label, stat in zip(labels[1:], character_stats[1:]):
        print(f"|{label:<12} | {stat:>10} |")
    print(f"{'-'*28}\n")
    #this function needs to return the character_stats list so that it can be used in the combat loop
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


def combat_loop(player_stats, enemy_stats):
    #initialize combat variables
    round_num = 1
    player_hp = int(player_stats[5])
    enemy_hp = int(enemy_stats[5])
    #combat loop
    while player_hp > 0 and enemy_hp > 0:
        print(f"\nRound {round_num}!")
        print(f"Player HP: {player_hp} | Enemy HP: {enemy_hp}\n")
        #choose action
        while True:
            try:
                #change action to chosing one of 5 options



#                action = int(input("Choose an action:\n1. Attack\n2. Defend\n3. Run\n"))
#                if action < 1 or action > 3:
#                    raise ValueError
#                break
#            except ValueError:
#                print("Invalid choice. Please try again.")
#        #player attacks
#        if action == 1:
#            player_attack = random.randint(1, int(player_stats[6]))
#            enemy_hp -= player_attack
#            print(f"You attack the enemy for {player_attack} damage!")
#        #player defends
#        elif action == 2:
#            player_defense = random.randint(1, int(player_stats[10]))
#            print(f"You defend yourself for {player_defense} damage!")


#        #player attacks
#        player_attack = random.randint(1, int(player_stats[6]))
#        enemy_hp -= player_attack
#        print(f"You attack the enemy for {player_attack} damage!")
#        #enemy attacks
#        enemy_attack = random.randint(1, int(enemy_stats[6]))
#        player_hp -= enemy_attack
#        print(f"The enemy attacks you for {enemy_attack} damage!")
        #increment round number
        round_num += 1






display_character_stats("Toon")
levels = list_levels()
chosen_level = load_level(levels)
print("Level chosen:", chosen_level)

