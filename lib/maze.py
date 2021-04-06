import pygame

from queue import deque
from random import choice

from .cell import (Cell, Wall, Start, End)


class Maze:
    def __init__(self, size):
        self.width = size[0] // Cell.width
        self.height = size[1] // Cell.height
        self.size = (self.width, self.height)
        self.path = []

        self.create_grid()

    def create_grid(self):
        self.grid = [
            [
                Wall(x, y, (self.width, self.height))
                for y in range(self.height)
            ] for x in range(self.width)
        ]

    def get(self, x, y):
        return self.grid[x][y]

    def set(self, cell):
        self.grid[cell.x][cell.y] = cell

    def set_start(self, screen):
        start = Start(self.path[0].x, self.path[0].y, self.size)
        self.set(start)
        start.draw(screen)
        pygame.display.update()

    def set_end(self, screen):
        end = End(self.path[-1].x, self.path[-1].y, self.size)
        self.set(end)
        end.draw(screen)
        pygame.display.update()

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def clean(self, screen):
        self.create_grid()
        self.draw(screen)

    def color_unvisited(self, unvisited):
        for cell in unvisited:
            cell.surf.fill((255, 0, 0))

    def get_random_neighbor(self, current, unvisited):
        return choice(
            [
                cell for cell in
                map(lambda x: self.get(*x), current.get_neighbors())
                if cell in unvisited
            ]
        )

    def generate(self, screen=None, animate=False, sleep=10):
        self.clean(screen)

        # Iterative implementation
        unvisited = [
            cell for row in self.grid for cell in row
            if cell.x % 2 and cell.y % 2
        ]

        current = unvisited.pop()
        stack = []

        while unvisited:
            try:
                neighbor = self.get_random_neighbor(current, unvisited)
                stack.append(current)

                x = current.x - (current.x - neighbor.x) // 2
                y = current.y - (current.y - neighbor.y) // 2

                current_cell = Cell(current.x, current.y, self.size)
                neighbor_cell = Cell(x, y, self.size)
                self.set(current_cell)
                self.set(neighbor_cell)
                self.path.append(current_cell)
                self.path.append(neighbor_cell)

                current = neighbor
                unvisited.remove(neighbor)

                if animate:
                    self.draw(screen)
                    pygame.display.update()
                    pygame.time.wait(sleep)
            except IndexError:
                if stack:
                    current = stack.pop()

        self.set_start(screen)
        self.set_end(screen)


    def search(self, screen=None, animate=False, sleep=10):
        pass
