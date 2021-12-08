from enum import Enum


class Position(Enum):
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"


class Color(Enum):
    BROWN = "#8b4513"
    LIGHT_BLUE = "sky_blue1"
    PINK = "#ffc0cb"
    ORANGE = "#ff8c00"
    RED = "#ff0000"
    YELLOW = "#ffd700"
    GREEN = "#008000"
    DARK_BLUE = "dark_blue"


class Icon(Enum):
    COMMUNITY_CHEST = "wrapped_gift"
    CHANCE = "question_mark"
    STATION = "steam_locomotive"
    LUXURY_TAX = "ring"
    ELECTRIC_COMPANY = "light_bulb"
    WATER_WORKS = "potable_water"
