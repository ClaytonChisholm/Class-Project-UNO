from enum import IntEnum


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

    def print(self):  # change with graphics
        if self.color != 0:  # checks that color isnt none
            print(str(self.color.name) + ' ' + str(self.type.name), end='')
        else:
            print(str(self.type.name), end='')
