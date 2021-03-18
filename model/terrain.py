from random import randint
import view

class Terrain():
    """ Contains information about the environment that the player moves around 
        in. """

    def _generate_map(height, width):
        return ['#' if randint(0, 10) > 5 else '.' for _ in range(width * height)]

    def __init__(self):
        self._size = (16, 16)
        self.grid = Terrain._generate_map(self._size[0], self._size[1])

    def get_tile(self, x, y):
        return self.grid[x + y * self.WIDTH]
    def get_tile(self, pos):
        return self.get_tile(pos[0], pos[1])

    #def get_area(self, pos, size):
    def get_area(self):
        return self.grid # for now

    def get_size(self):
        return self._size

    def display(self):
        height, width = self.get_size()
        for y in range(0, height):
            for x in range(0, width):
                view.put(self.get_tile(x, y), end=" ")
            view.newline()