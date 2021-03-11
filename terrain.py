import random

class Terrain():
    """ Contains information about the environment that the player moves around 
        in. """

    def _generate_map(width, height):
        return ['#' if random.randint(0, 10) > 5 else '.' for _ in range(width * height)]

    def __init__(self):
        self.WIDTH, self.HEIGHT = 16, 16
        self.grid = Terrain._generate_map(self.WIDTH, self.HEIGHT)

    def get_tile(self, x, y):
        return self.grid[x + y * self.WIDTH]

    def display(self):
        for y in range(0, self.HEIGHT):
            for x in range(0, self.WIDTH):
                print(self.get_tile(x, y), end=" ")
            print("\n", end="")