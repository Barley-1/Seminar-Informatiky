#!/usr/bin/env python3

import dice
import ship

d = dice.Dice(10)
def get_status():
    return f'ship.Ship.get_status()'
  
ship1 = ship.Ship("Destroyer", 100, 20, 18, d, get_status())
ship2 = ship.Ship("Cruiser", 100, 15, 22, d, get_status())

ship1.attack_roll(ship2)
print(ship1.get_status())
print(ship2.get_status())
