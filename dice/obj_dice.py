#!/usr/bin/env python3

import random

class Dice:
    def __init__(self, sides):
            self.sides = sides

    def roll(self):
        return(random.randint(1,self.sides))

def main():
    d4 = Dice(4)
    d6 = Dice(6)
    d8 = Dice(8)
    d10 = Dice(10)
    d12 = Dice(12)
    d20 = Dice(20)
    d100 = Dice(100)
    print(d4.roll())
    print(d6.roll())
    print(d8.roll())
    print(d10.roll())
    print(d12.roll())
    print(d20.roll())
    print(d100.roll())


if __name__ == '__main__':
    main()