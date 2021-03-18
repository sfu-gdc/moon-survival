from model.types import Direction, Vector2D

class Player():
    MOVE_OFFSET = {
        Direction.North: Vector2D(0, -1),
        Direction.East: Vector2D(1, 0),
        Direction.South: Vector2D(0, 1),
        Direction.West: Vector2D(-1, 0) }

    def __init__(self):
        self._position = Vector2D(0, 0)
        self._icon = "@"

        self.hp = 10
        self.max_hp = 10

    def get_position(self):
        return self._position

    def get_icon(self):
        return self._icon

    def move(self, direction):
        self._position += Player.MOVE_OFFSET[direction]
        print(self._position)