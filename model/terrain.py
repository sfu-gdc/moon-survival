from random import randint
from util import randint_around
from mytypes import Vector2D, Matrix2D, Buffer2D, TileMaterial, TileDetail

import view

class Terrain():
    """ Contains information about the environment that the player moves around 
        in. """

    def __init__(self):
        self.SIZE = Vector2D(100, 100)
        self._generate_map(self.SIZE)

    # should only be caled once.
    def _generate_map(self, size):
        height_list = [1 for _ in range(size.x * size.y)]
        self.height_grid = Matrix2D.from_list(size, height_list)

        detail_list = [TileDetail.Rock if randint(0, 10) > 8 else TileDetail.Ground for _ in range(size.x * size.y)]
        self.detail_grid = Matrix2D.from_list(size, detail_list)

        self.mat_grid = Matrix2D(size, TileMaterial.MoonRock)

        # 1 vent for each 10sq meters +- 2 ~ TODO: update to 100 sq meters or larger.
        geothermal_vent_dispersion_area = 10 * 10
        num_geothermal_vents = randint_around(size.x * size.y // geothermal_vent_dispersion_area, 2) 
        for _ in range(0, num_geothermal_vents):
            x, y = randint(0, size.x-1), randint(0, size.y-1)
            self.mat_grid.set(Vector2D(x, y), TileMaterial.GeothermalVent)

        pass

    def get_tile(self, pos):
        return self.grid.get(pos)

    # size needs to be even to divide nicely - TODO: decide about this
    def get_area(self, pos, size):
        map_buf = Buffer2D(size)
        bot, top = pos.y - size.y // 2, pos.y + size.y // 2
        left, right = pos.x - size.x // 2, pos.x + size.x // 2
        for y in range(bot, top):
            for x in range(left, right):
                detail = TileDetail.Map[self.detail_grid.get_else(Vector2D(x, y), TileDetail.Void)]
                tile_txt = detail
                map_buf.set(Vector2D(x - left, y - bot), tile_txt) # normalized coordinates
        return map_buf

    def get_area_color(self, pos, size):
        map_buf = Buffer2D(size)
        bot, top = pos.y - size.y // 2, pos.y + size.y // 2
        left, right = pos.x - size.x // 2, pos.x + size.x // 2
        for y in range(bot, top):
            for x in range(left, right):
                material = TileMaterial.Map[self.mat_grid.get_else(Vector2D(x, y), "none")]
                detail = TileDetail.Map[self.detail_grid.get_else(Vector2D(x, y), TileDetail.Void)]
                tile_txt = view.color(detail, material)
                map_buf.set(Vector2D(x - left, y - bot), tile_txt)
        return map_buf

    def display(self):
        width, height = self.grid.size
        for y in range(0, height):
            for x in range(0, width):
                view.put(self.get_tile(Vector2D(x, y)), end=" ")
            view.newline()