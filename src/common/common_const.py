from enum import Enum

class WaitTime(Enum):
    LONG = 5
    SHORT = 2

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"