from enum import Enum

class Direction(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

class TileMaterial():
    MoonRock = 1
    MoonDust = 2
    LunarOil = 3
    GeothermalVent = 4
    MoonMetal = 5
    Copper = 6
    Gold = 7

    Map = {
        MoonRock: "none",
        MoonDust: "_w",
        LunarOil: "_bk",
        GeothermalVent: "_r",
        MoonMetal: "_bb",
        Copper: "_c",
        Gold: "_y",
    }

class TileDetail():
    Ground = 0
    Rock = 1
    Void = 2

    Map = {
        Ground: '.',
        Rock: '&',
        Void: 'V'
    }

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(a, b):
        return Vector2D(a.x + b.x, a.y + b.y)

    def __getitem__(self, key):
        return self.x if key == 0 else self.y

    def __iter__(self):
        return iter([self.x, self.y])

    def __repr__(self):
        return "x, y: " + str(self.x) + ", " + str(self.y)

class Matrix2D():
    def from_list(size, list):
        m = Matrix2D(size, 0)
        m.fill(list)
        return m

    def from_mat(mat):
        m = Matrix2D(mat.size, 0)
        m.fill(mat.contents.copy())
        return m
    
    def __init__(self, size, default_el):
        self.size = size
        self.contents = [default_el for _ in range(size.x * size.y)]

    # takes list as its own
    def fill(self, list):
        if len(list) == len(self.contents):
            self.contents = list
        else:
            raise Exception("Invalid list size for filling")

    # loc should be a vec2 & inside size.
    def set(self, loc, ch):
        self.contents[loc.x + loc.y * self.size.x] = ch

    def get(self, loc):
        return self.contents[loc.x + loc.y * self.size.x]

    # if index is invalid, returns default.
    def get_else(self, loc, default):
        index = loc.x + loc.y * self.size.x
        if index >= 0 and index < self.size.x * self.size.y:
            return self.contents[loc.x + loc.y * self.size.x]
        else:
            return default

    def __str__(self):
        out = ""
        for y in reversed(range(self.size.y)):
            for x in range(self.size.x):
                out += self.get(Vector2D(x, y))
            out += "\n"
        return out

'''
    def putc(self):
        for y in reversed(range(self.size.y)):
            for x in range(self.size.x):
                view.putc(self.contents[x + y * self.size.x])
            view.newline()
'''

class Buffer2D(Matrix2D):
    ''' 
        Stores a matrix of characters to mutate before drawing to the screen. 
    '''

    def __init__(self, size, default=" "):
        super().__init__(size, default)

    # skips newlines
    def fill(self, txt):
        self.contents = [ch for ch in txt if ch in "\n" and ch != "\r"]
