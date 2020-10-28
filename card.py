from enum import IntEnum
from colored import fg, bg, attr
# TODO pip3 install colored, put this in readme


class Color(IntEnum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Type(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    SKIP = 10
    REVERSE = 11
    DRAW2 = 12
    WILD = 13
    DRAW4 = 14


class Card:

    def __init__(self, card_type: Type, color: Color = Color.NONE):  # defaults to no color
        self.type = card_type
        self.color = color

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def set_wild(self, color: Color):  # sets the color f a card if it is determined to be a wild card.
        if self.get_type() == Type.WILD or self.get_type() == Type.DRAW4:
            self.color = color

    def print(self):  # change with graphics  for some reason a black foreground shows up as white but whatever
        reset = attr('reset')
        if self.color == 0:  # checks that color isn't none
            color = bg('black') + fg('white')
        elif self.color == 1:
            # print(colored(, 'red', end='')else
            color = bg('red') + fg('white')
        elif self.color == 2:
            # print(colored(str(self.type.name).capitalize(), 'dark_green'), end='')
            color = bg('green_4') + fg('white')
        elif self.color == 3:
            # print(colored(str(self.type.name).capitalize(), 'blue'), end='')
            color = bg('dodger_blue_2') + fg('white')
        else:
            # print(colored(str(self.type.name).capitalize(), 'yellow'), end='')
            color = bg('yellow') + fg('white')
            # print(str(self.type.name).capitalize(), end='')
        if self.type < 12:
            print(color + attr('bold') + str(self.color.name).capitalize() + ' ' + str(self.type.name).capitalize() + reset, end='')
        else:
            print(color + str(self.type.name).capitalize() + reset, end='')

