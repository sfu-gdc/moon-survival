from terrain import Terrain

class World():
    def __init__(self):
        self.terrain = Terrain()
        pass

    def display_terrain(self):
        self.terrain.display()