import os
import csv
import random

def display_character_stats(character_name):
    # Load character stats from CSV file    
    with open(f"{character_name}.csv", "r") as character_file:
        character_reader = csv.reader(character_file)
        character_stats = next(character_reader)  # read only the first line of the file
    # Display character's stats in a table
    labels = ["Name", "Height", "Weight", "Size", "XP", "HP", "Stam", "Mana", "Agil", "Defc", "Jump"]
    print(f"\n{'-'*45}")
    print(f"|{labels[0]:<12} | {character_stats[0]:>10} |")
    print(f"{'-'*45}")
    for label, stat in zip(labels[1:], character_stats[1:]):
        print(f"|{label:<12} | {stat:>10} |")
    print(f"{'-'*45}\n")



