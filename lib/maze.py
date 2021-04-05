import pygame

from cell import Cell
from wall import Wall


class Maze:
    def __init__(self, size):
        self.width = size[0] // Cell.width,
        self.height = size[1] // Cell.height
        self.grid = []

    def get(self, x, y):
        return self.grid[x][y]

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)
