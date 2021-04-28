import random as rand
import Randomizer   # Custon Dice Module
import Dev_Cards    # Custom Deck of Cards and controls
#import tkinter as tk

### Setup ###

num_players = None
players_devcards = None
player_resources = None

### Functions ###


'''TODO: build a map seed that generates in a spiral
->  1 1 1
   1 1 1 1
^ 1 1 1 1 1 v
   1 1 1 1 
    1 1 1 
     <  

figure out seeding the map with a random generation in a spiral
'''

def gen_map():
  # lay tiles
  # number the tiles
  # port locations should be fixed, not random
  pass

# randomizer controls DiceRoll()!

def get_Resources(roll):
  # find tiles with matching number
  # check for settlements and cities adjacent to tile
  # give resources: 1 per settlement, 2 per city
  pass

def trade():
  # original 4:1
  # port specific 3:1 or special 2:1
  # with another player
  pass

def build():
  # purchase something
  # place or upgrade
  pass

### Initialize ###

roll = Randomizer.DiceRoll()

print(roll)