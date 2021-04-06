import heapq
import pygame

from .cell import Wall


class Astar:
    def __init__(self, maze, screen=None, animate=False, sleep=1):
        self.maze = maze
        self.screen = screen
        self.animate = animate
        self.sleep = sleep

    def _return_path(self, current):
        path = []
        current = current.parent

        while current != self.maze.start:
            path.append(current)
            current.surf.fill((0, 255, 255))
            if self.animate:
                current.draw(self.screen)
                pygame.display.update()
                pygame.time.wait(self.sleep)

            current = current.parent

        return path[::-1]

    def heuristic(self, current, other, type='euclidian'):
        h = 0

        if type == 'euclidian':
            h = ((current.x - other.x)**2) + ((current.y - other.y)**2)

        return h

    def add_to_open(self, open, neighbor):
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

    def search(self):
        open = []
        closed = []

        heapq.heapify(open)
        heapq.heappush(open, self.maze.start)

        while len(open) > 0:
            # Step 1
            current = heapq.heappop(open)
            closed.append(current)

            if current == self.maze.end:
                return self._return_path(current)

            # Step 2
            neighbors = current.get_neighbors()

            # Step 3
            for neighbor in neighbors:
                cell = self.maze.get(*neighbor)

                if type(cell) == Wall:
                    continue

                if cell in closed:
                    continue

                cell.parent = current
                cell.g = current.g + 1
                cell.h = self.heuristic(
                    current, self.maze.end, type='euclidian'
                )
                cell.f = cell.g + cell.h

                if self.add_to_open(open, cell):
                    heapq.heappush(open, cell)

            closed.append(current)

            if current not in (self.maze.start, self.maze.end):
                current.surf.fill((0, 0, 255))

            if self.animate:
                current.draw(self.screen)
                pygame.display.update()
                pygame.time.wait(self.sleep)

        return None
