from .cell import Cell


class Wall(Cell):
    def __init__(self, x, y, maze_size):
        super(Wall, self).__init__(x, y, maze_size)
        self.surf.fill((0, 0, 0))

    def __str__(self):
        return f'Wall: ({self.x},{self.y})'
