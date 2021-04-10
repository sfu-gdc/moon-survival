from mytypes import Vector2D
from model.terrain import Terrain
from model.player import Player

import view

class World():
    def __init__(self):
        self.terrain = Terrain()
        self.player = Player(self)

    # --------------------------------------------------- #

    def get_map_size(self):
        return self.terrain.SIZE

    # --------------------------------------------------- #

    def display_terrain(self):
        view.putln("Displaying Scanned Terrain Data: ")
        self.terrain.display()

    def display_map(self):
        view.putln("Displaying Map: ")

        map_buf = self.terrain.get_area(self.player.position, view.Size)

        center = Vector2D(view.Size.x // 2, view.Size.y // 2)
        map_buf.set(center, self.player.icon)
        view.put(map_buf)

    def display_scanned_map(self):
        view.putln("Displaying Scanned Map: ")

        map_buf = self.terrain.get_area_color(self.player.position, view.Size)

        center = Vector2D(view.Size.x // 2, view.Size.y // 2)
        map_buf.set(center, self.player.icon)
        view.put(map_buf)

    def move_player(self, direction):
        self.player.move(direction)
