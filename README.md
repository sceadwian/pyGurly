# pyGurly
Primeiro Projeto em Python usando GitHub

![Front Image](./images/alice.jpg "Alice")

-=-=-=-=-=-
Game design

Select character
Characters <- saved in a CSV file . File name should be "character_name.txt" based on name of character

Shows character profile -> select  level you would like to play
Levels shown based on reading the folder for any files that start with the work map_01-Level 1

Levels  <- available to be loaded as CSV files with first ??? lines being the map and the last ??? lines define different aspects of map such as loot and mobs?
        opt. potentially make this into a text based game perhaps??? I think this is actually what i'll do for now. Maybe later on we can add so that instead of selecting it through text, we actually have little csv maps we can use.
        
Once player picks the level, there are 3 battles. Battle 1 and battle 2 are given to the player randomly from a list of potential foes. There should be a list of mobs for these types of fights and then battle 3 is against the boss

-=-=-=-=-=-
Character

previous_py
name,cut,bleed,blunt,poison,curse,fire,P-def,M-def,ATK,HP

name = Toon
height = 
weight = 
size = (mix of height and weight) - small stature good for some things like avoiding attacks, but being tall should have some benefit in some of the attacks
xp = 0
hp = 5
stam = 10
strg = 5
magk = 5
agil = 5
intl = 5
defc = 5
jump = 5


Map / Level information
stored in map_*.csv
contains: level_name, level_actions_ID, boss_ID, mob1_ID, mob2_ID_mob3_ID, mob4_ID, mob5_ID, mob6_ID

level_actions_ID <-- draw from own_actions.csv #20230430 should I just do away with mob/own actions and just have the actions live in the combat_loop?
mob_actions <-- stores actions used by mobs and bosses
own_actions <-- stores actions available to users, maybe instead of level_actions.csv, I should just use this as source file???
boss_ID <-- draw from level_boss.csv
mob1_ID <-- draw from level_mob.csv

mob_ID / boss_ID - name, height, weight, size, xp, hp, stam, strg, mgk, agil, dfc, jump,(then 5 id actions) maybe each mob will go through each of the actions in sequential order? mob actions maybe should be stored separately from the player actions? ... also should actions be stored in the main py or in support files?

-=-=-=-=-=-
Combat

Each round each character picks an action from a list that he/she has been building up through battles

--> action (-stam, damage, block, protection ,heal)
--> Punch
--> Kick
--> Block (1,0,defc)
--> Recover (recovers +1 stam)
--> Bash
--> Rest Block (recovers +2 stam)
--> Defensive Punch
--> Roundhouse kick
--> heal (recovers +1 stam +? HP)



Action is resolved delivering damage to each fighter
Action takes certain amount of stamina but +1 recovered p/ round.
Each character has many attributes
Attributes used to execute different attacks
Attack's efficacy based
-=-=-=-=-=-
interesting idea combat mechanics
https://boardgamegeek.com/thread/2119138/most-fun-combat-mechanics
Matt Price
@mattprice
Dec 26, 2018
A simple system that I've recently discovered is that in Dungeon Degenerates. I've not seen it implemented elsewhere.
The attacker makes one roll vs. the defender (monsters in the game, there is no PvP) using standard d6s. Two d6 are one color (attack), two are another (defense) and there are up to two more ("power"). In order to hit the monster, your attack dice must be equal to or below a value (typically your hero's strength, but this depends on the weapon being used) and similarly, in order to block incoming hits your defense roll must also be equal to or below a value (typically agility, but this can also vary). What's neat is that one die's value of the resultant roll is the damage delivered (attack) or resisted (defense). So you want to roll low to pass your check, but you'd like one die's value to be high, so you block lots or delivery a good smackdown.
Now add to this your stance at the outset. If you choose a guarded stance, you add one power die. That die may be used as part of your defense roll (essentially, you swap it out for one of the other two) to give you a better chance to defend. Or if you choose an assault stance, you do the same but with your attack roll.
Some magical weapons or conditions allow you to roll two power dice, and create an optimal roll using four attack or defense dice.
There's a bit more to it, but overall that's it and it's super neat. And once you get it down, it goes very quickly: it's just declaring your stance, and rolling your dice.
(I think the rules are available online or on the BGG page for DD)


