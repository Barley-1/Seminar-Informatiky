#!/usr/bin/env python3

from dice import Dice
from ship import Ship

class BattleGame:
    def __init__(self, ship1, ship2, dice):
        self._ship1 = ship1
        self._ship2 = ship2
        self._dice = dice
    
    def _ship_status(self, ship):
        print(ship)
        print(f'Hull Integrity: {ship._size}')

    def start_battle(self):
        import random
        print("Welcome to the Battle!")
        print("======================\n")
        print(f'The ships {self._ship1} and {self._ship2} will fight today!')
        print("Starting battle...")
        input()
        while self._ship1._size > 0 and self._ship2._size > 0:
            self._ship1.attack_roll(self._ship2)
            self.visual_battle()
            self._print_status(self._ship1.get_status())
            self._print_status(self._ship2.get_status())
            self._ship_status(self._ship2)

            if self._ship2._size > 0:
                self._ship2.attack_roll(self._ship1)
                self.visual_battle()
                self._print_status(self._ship2.get_status())
                self._print_status(self._ship1.get_status())
                self._ship_status(self._ship1)

    def _print_status(self, status):
        import time as _time
        if status:
            print(status)
            _time.sleep(0.5)
    
    def _clear_screen(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.cal(['cmd.exe', '/c', 'cls'])
        else:
            _subprocess.call(['clear'])

    def visual_battle(self):
        self._clear_screen()
        print('====================== Sektor Orion ======================')
        print('Ships:\n')
        self._ship_status(self._ship1)
        self._ship_status(self._ship2)
        print()

if __name__ == '__main__':
    d = Dice(10)
    def get_status():
        return f'ship.Ship.get_status()'
  
    ship1 = Ship("Destroyer", 100, 20, 18, d, get_status())
    ship2 = Ship("Cruiser", 100, 15, 22, d, get_status())

    game = BattleGame(ship1, ship2, d)
    game.start_battle()
