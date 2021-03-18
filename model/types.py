from enum import Enum

# python 3.4 earliest support
class Direction(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

class Vector2D():
    def __init__(self, x, y):
        self._pos = (x, y)

    def __add__(a, b):
        return Vector2D(a._pos[0] + b._pos[0], a._pos[1] + b._pos[1])

    def __getitem__(self, key):
        return self._pos[key]

    def __repr__(self):
        return "pos: " + str(self._pos)