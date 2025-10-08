#!/usr/bin/env python3
import random

class Dice:
    def __init__(self, sides):
        self.__sides = sides

    def __str__(self):
        return f'D{self.__sides}'

    def roll(self):
        return random.randint(1, self.__sides)

def main():
    d6 = Dice(6)
    print(d6.roll())

if __name__ == '__main__':
    main()