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
        self._status = ''

    def __str__(self):
        return str(self._name)

    def attack_roll(self, opponent):
        attack_rolls = self._attack + self._dice.roll()
        status_report = f'{self._name} shoots its cannons dealing {attack_rolls} damage.'
        self.set_status(status_report)
        opponent.defend_roll(attack_rolls)

    
    def defend_roll(self, attack_rolls):
        damage = attack_rolls - (self._defense + self._dice.roll())
        if damage > 0:
            status_report = f'{self._name} takes {damage} damage to the hull!'
            self._size -= damage
        else:
            status_report = f'{self._name} evaded the attack!'
        self.set_status(status_report)

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

if __name__ == '__main__':
    main()