from mytypes import Direction, Vector2D

class Player():
    MOVE_OFFSET = {
        Direction.North: Vector2D(0, -1),
        Direction.East: Vector2D(1, 0),
        Direction.South: Vector2D(0, 1),
        Direction.West: Vector2D(-1, 0) }

    def __init__(self):
        self.position = Vector2D(0, 0)
        self.icon = "@"

        self.hp = 10
        self.max_hp = 10

    def move(self, direction):
        self.position += Player.MOVE_OFFSET[direction]
        print(self.position)