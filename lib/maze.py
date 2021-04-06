import heapq
import pygame

from queue import deque
from random import choice

from .cell import (Cell, Wall, Start, End)


class Maze:
    def __init__(self, size):
        self.width = size[0] // Cell.width
        self.height = size[1] // Cell.height
        self.size = (self.width, self.height)
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

    def set_start(self, screen):
        cell = self.get(-2, -2)
        start = Start(cell.x, cell.y, self.size)
        self.start = start
        self.set(start)
        start.draw(screen)
        pygame.display.update()

    def set_end(self, screen):
        cell = self.get(1, 1)
        cells = [(2, 1), (1, 2), (2, 2)]
        i = 0
        while type(cell) != Cell:
            x, y = cells[i]
            cell = self.get(x, y)
            i += 1

        end = End(cell.x, cell.y, self.size)
        self.end = end
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

                if animate:
                    self.draw(screen)
                    pygame.display.update()
                    pygame.time.wait(sleep)
            except IndexError:
                if stack:
                    current = stack.pop()

        self.set_start(screen)
        self.set_end(screen)

        print('finished')


    def astar_search(self, screen=None, animate=False, sleep=10):
        open = []
        closed = []

        heapq.heapify(open)
        heapq.heappush(open, self.start)
        print(open)

        while len(open) > 0:
            # Step 1
            current = heapq.heappop(open)
            current.surf.fill((0, 0, 255))
            closed.append(current)

            print(current)
            if current == self.end:
                path = []
                while current is not None:
                    path.append((current.x, current.y))
                    current = current.parent
                return path[::-1]  

            # Step 2 & 3
            children = []
            neighbors = current.get_neighbors(1)

            for neighbor in neighbors:
                neighbor_cell = self.get(*neighbor)
                if type(neighbor_cell) == Wall:
                    continue
                children.append(neighbor_cell)

            for child in children:
                if len([closed_child for closed_child in closed if closed_child == child]) > 0:
                    continue

                child.g = current.g + 1
                child.h = ((child.x - self.end.y) ** 2) + ((child.x - self.end.y) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                if len([open_node for open_node in open if child == open_node and child.g > open_node.g]) > 0:
                    continue

                # Add the child to the open list
                heapq.heappush(open, child)

            if animate:
                self.draw(screen)
                pygame.display.update()
                pygame.time.wait(sleep)

        return None
