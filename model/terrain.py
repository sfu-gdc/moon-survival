from random import randint

from mytypes import Vector2D, Matrix2D

import view

class Terrain():
    """ Contains information about the environment that the player moves around 
        in. """

    def _generate_map(size):
        return Matrix2D.from_list(size, ['#' if randint(0, 10) > 5 else '.' for _ in range(size.x * size.y)])

    def __init__(self):
        self.grid = Terrain._generate_map(Vector2D(16, 16))

    def get_tile(self, pos):
        return self.grid.get(pos)

    #def get_area(self, pos, size):
    def get_map(self):
        return self.grid # for now

    def display(self):
        width, height = self.grid.size
        for y in range(0, height):
            for x in range(0, width):
                view.put(self.get_tile(Vector2D(x, y)), end=" ")
            view.newline()