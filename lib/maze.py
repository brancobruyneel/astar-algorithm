import pygame

from queue import deque
from random import choice

from lib.cell import (Cell, Wall)


class Maze:
    def __init__(
        self, size, diagonal=False, screen=None, animate=False, sleep=1
    ):
        self.width = size[0] // Cell.width
        self.height = size[1] // Cell.height
        self.size = (self.width, self.height)

        self.diagonal = diagonal

        self.screen = screen
        self.animate = animate
        self.sleep = sleep

        self.start = None
        self.end = None

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

    def set_start(self):
        start = Cell(self.width - 2, self.height - 2, self.size)
        self.start = start
        self.set(start)

        start.surf.fill((0, 255, 0))
        start.draw(self.screen)
        pygame.display.update()

    def set_end(self):
        cell = self.get(1, 1)
        cells = [(2, 1), (1, 2), (2, 2)]
        i = 0
        while type(cell) != Cell:
            x, y = cells[i]
            cell = self.get(x, y)
            i += 1

        end = Cell(cell.x, cell.y, self.size)
        self.end = end
        self.set(end)

        end.surf.fill((255, 0, 0))
        end.draw(self.screen)
        pygame.display.update()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw(self.screen)

    def clean(self):
        self.create_grid()
        self.draw()

    def color_unvisited(self, unvisited):
        for cell in unvisited:
            cell.surf.fill((255, 0, 0))

    def get_random_neighbor(self, current, unvisited):
        return choice(
            [
                cell for cell in
                map(lambda x: self.get(*x), current.get_neighbors(2))
                if cell in unvisited
            ]
        )

    def generate(self):
        self.clean()

        # Iterative implementation
        unvisited = [
            cell for row in self.grid for cell in row
            if cell.x % 2 and cell.y % 2
        ]

        current = unvisited.pop()
        stack = deque()

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

                current = neighbor
                unvisited.remove(neighbor)

                if self.animate:
                    current_cell.draw(self.screen)
                    neighbor_cell.draw(self.screen)
                    pygame.display.update()
                    pygame.time.wait(self.sleep)

            except IndexError:
                if stack:
                    current = stack.pop()

        self.set_start()
        self.set_end()
