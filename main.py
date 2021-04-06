import logging
import pygame

from pygame.locals import (
    K_r,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from lib.cell import Cell
from lib.maze import Maze

logging.basicConfig(level=logging.ERROR)

pygame.init()

WINSIZE = (Cell.width * 41, Cell.height * 41)

screen = pygame.display.set_mode(WINSIZE)
clock = pygame.time.Clock()

maze = Maze(WINSIZE)


def draw_maze():
    maze.draw(screen)
    maze.generate(screen, True, 1)
    print(maze.astar_search(screen, True, 10))


draw_maze()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_r:
                draw_maze()
            if event.key == K_SPACE:
                # A* Search Algorithm
                pass
            elif event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pygame.display.flip()
    clock.tick()
