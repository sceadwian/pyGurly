import os
import csv
import random

def display_character_stats(character_name):
    # Load character stats from CSV file    
    with open(f"{character_name}.csv", "r") as character_file:
        #what does f do here?
        #    
        character_reader = csv.reader(character_file)
        character_stats = next(character_reader)  # read only the first line of the file
    # Display character's stats in a table
    labels = ["Name", "Height", "Weight", "Size", "XP", "HP", "Stam", "Magk", "Agil", "Defc", "Jump"]
    print(f"\n{'-'*28}")
    print(f"|{labels[0]:<12} | {character_stats[0]:>10} |")
    print(f"{'-'*28}")
    for label, stat in zip(labels[1:], character_stats[1:]):
        print(f"|{label:<12} | {stat:>10} |")
    print(f"{'-'*28}\n")

def list_levels():
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

# write a function that asks user to select a level and then loads it
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
    level_chosen = load_level(levels[level_choice-1])
    return level


display_character_stats("Toon")

list_levels()

levels = ["Level 1", "Level 2", "Level 3"]
chosen_level = load_level(levels)
print("Level chosen:", chosen_level)

