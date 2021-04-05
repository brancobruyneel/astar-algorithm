from .cell import Cell


class Wall(Cell):
    def __init__(self, x, y):
        super(Wall, self).__init__(x, y)
        self.surf.fill((0, 250, 0))
