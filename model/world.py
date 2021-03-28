from mytypes import Vector2D, Buffer2D
from model.terrain import Terrain
from model.player import Player

import view

class World():
    def __init__(self):
        self.terrain = Terrain()
        self.player = Player()

    def display_terrain(self):
        view.putln("Displaying Scanned Terrain Data: ")
        self.terrain.display()

    def display_map(self):
        view.putln("Displaying Map: ")

        map = self.terrain.get_map()
        buf = Buffer2D.from_mat(map)

        buf.set(self.player.position, self.player.icon)
        buf.put()

    def move_player(self, direction):
        self.player.move(direction)
