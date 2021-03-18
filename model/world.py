from model.terrain import Terrain
from model.player import Player
from model.util import mat2dset

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
        area = self.terrain.get_area()
        width, height = self.terrain.get_size()
        view.putmat2d(area, (width, height))
        
        x, y = self.player.get_position()
        view.putat((width - x, height - y), self.player.get_icon())

    def move_player(self, direction):
        self.player.move(direction)
