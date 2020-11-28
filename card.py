from enum import IntEnum
from colored import fg, bg, attr


# enum for card color
class Color(IntEnum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


# enum for type of cards
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

    def __init__(self, card_type: Type, color: Color = Color.NONE):  # defaults to no color, eg wilds
        self.type = card_type
        self.color = color

    # returns card type
    def get_type(self):
        return self.type

    # returns card color
    def get_color(self):
        return self.color

    def set_wild(self, color: Color):  # sets the color of a card if it is determined to be a wild card.
        if self.get_type() == Type.WILD or self.get_type() == Type.DRAW4:
            self.color = color

    def get_path(self):
        path = 'cards/'
        if self.color == Color.RED:
            path += 'red_'
        elif self.color == Color.GREEN:
            path += 'green_'
        elif self.color == Color.BLUE:
            path += 'blue_'
        elif self.color == Color.YELLOW:
            path += 'yellow_'

        if self.type.value < 10:
            path += str(self.type.value) + '.png'
        elif self.type.value == 10:
            path += 'skip.png'
        elif self.type.value == 11:
            path += 'reverse.png'
        elif self.type.value == 12:
            path += 'picker.png'
        elif self.type.value == 13:
            path += 'wild.png'
        else:
            path += 'wild_pick_four.png'

        return path
