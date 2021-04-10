from mytypes import Direction, Vector2D
import view

class Player():
    MOVE_OFFSET = {
        Direction.North: Vector2D(0, 1),
        Direction.East: Vector2D(1, 0),
        Direction.South: Vector2D(0, -1),
        Direction.West: Vector2D(-1, 0) }

    def __init__(self, world):
        width, height = world.get_map_size()
        self.position = Vector2D(width // 2, height // 2)
        self.icon = "@"

        self.hp = 10
        self.max_hp = 10

        self.power = 10
        self.max_power = 10

    def display_stats(self):
        view.putcln("{bm}hp{}:" + "\t{}/{}".format(self.hp, self.max_hp))
        view.putcln("{by}power{}:" + "\t{}/{}".format(self.power, self.max_power))

    # This function is meant to scan the environment and use up a bit of power.
    def full_scan(self):
        pass
        self.power -= 10

    def weak_scan(self, level=1):
        pass
        self.power -= level

    def move(self, direction):
        self.position += Player.MOVE_OFFSET[direction]
        print(self.position)