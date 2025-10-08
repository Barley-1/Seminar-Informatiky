#!/usr/bin/env python3

'''
Ship class for battle game
'''

class Ship:
    '''
    Represents a ship with attributes like name, size, attack, defense, and dice.
    '''
    def __init__(self, name, size, attack, defense, dice, status):
        self._name = name
        self._size = size
        self._attack = attack
        self._defense = defense
        self._dice = dice
        self._status = status

    def __str__(self):
        '''
        Returns the string representation of the ship.
        '''
        return str(self._name)

    def attack_roll(self, opponent):
        '''
        Simulates an attack roll against an opponent ship.
        '''
        attack_rolls = self._attack + self._dice.roll()
        opponent.defend_roll(attack_rolls)
        status_report = f'{self._name} shoots its cannons dealing {attack_rolls} damage.'

    
    def defend_roll(self, attack_rolls):
        '''
        Simulates a defense roll against an opponent ship's attack.
        '''
        defense_rolls = self._defense + self._dice.roll()
        damage = attack_rolls - defense_rolls
        if damage > 0:
            status_report = f'{self._name} takes {damage} damage to the hull!'
            self._size -= damage
        else:
            status_report = f'{self._name} evaded the attack!'
            self.set_status(status)

    def set_status(self, status):
        '''
        Sets the status of the ship.
        '''
        self._status = status

    def get_status(self):
        '''
        Returns the current status of the ship.
        '''
        return self._status

if __name__ == "__main__":
    main()