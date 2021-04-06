import pygame

from queue import deque
from random import choice

from .cell import Cell
from .wall import Wall


class Maze:
    def __init__(self, size):
        self.width = size[0] // Cell.width
        self.height = size[1] // Cell.height
        self.grid = [
            [
                Wall(x, y, (self.width, self.height))
                for y in range(self.height)
            ] for x in range(self.width)
        ]

    def get(self, x, y):
        return self.grid[x][y]

    def set(self, x, y, cell):
        self.grid[x][y] = cell

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def generate(self, screen=None, animate=False, sleep=10):
        # Iterative implementation
        unvisited = [
            cell for row in self.grid for cell in row
            if cell.x % 2 and cell.y % 2
        ]
        current = unvisited.pop()
        stack = deque()

        while unvisited:
            try:
                next = choice(
                    [
                        cell for cell in
                        map(lambda x: self.get(*x), current.get_neighbors())
                        if cell in unvisited
                    ]
                )
                stack.append(current)
                x = current.x - (current.x - next.x) // 2
                y = current.y - (current.y - next.y) // 2

                size = (self.width, self.height)
                self.set(x, y, Cell(x, y, size))
                self.set(
                    current.x, current.y,
                    Cell(current.x, current.y, size)
                )

                current = next
                unvisited.remove(next)

                if animate:
                    self.draw(screen)
                    pygame.display.update()
                    pygame.time.wait(sleep)
            except IndexError:
                if stack:
                    current = stack.pop()
