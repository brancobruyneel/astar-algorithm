import pygame


class Cell(pygame.sprite.Sprite):
    width = 16
    height = 16

    def __init__(self, x, y, maze_size, parent=None):
        super(Cell, self).__init__()
        self.surf = pygame.Surface([self.width, self.height])
        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()
        self.rect.x = x * self.width
        self.rect.y = y * self.width

        self.x = x
        self.y = y

        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

        self.maze_width = maze_size[0]
        self.maze_height = maze_size[1]

    def get_neighbors(self, d=2, diagonal=False):
        if diagonal:
            x_axis = [0, d, 0, -d, d, -d, d, -d]
            y_axis = [d, 0, -d, 0, d, -d, -d, d]
        else:
            x_axis = [0, d, 0, -d]
            y_axis = [d, 0, -d, 0]

        return [
            (self.x + x, self.y + y) for x, y in zip(x_axis, y_axis)
            if 0 <= self.x + x < self.maze_width and 0 <= self.y +
            y < self.maze_height
        ]

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __str__(self):
        return f'Cell: ({self.x},{self.y})'

    def __repr__(self):
        return str(self)


class Wall(Cell):
    def __init__(self, x, y, maze_size):
        super(Wall, self).__init__(x, y, maze_size)
        self.surf.fill((0, 0, 0))

    def __str__(self):
        return f'Wall: ({self.x},{self.y})'


class Start(Cell):
    def __init__(self, x, y, maze_size):
        super(Start, self).__init__(x, y, maze_size)
        self.surf.fill((0, 255, 0))

    def __str__(self):
        return f'Start: ({self.x},{self.y})'


class End(Cell):
    def __init__(self, x, y, maze_size):
        super(End, self).__init__(x, y, maze_size)
        self.surf.fill((255, 0, 0))

    def __str__(self):
        return f'End: ({self.x},{self.y})'
