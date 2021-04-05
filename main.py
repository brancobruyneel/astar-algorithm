import pygame

from pygame.locals import QUIT

from lib.cell import Cell
from lib.maze import Maze

pygame.init()

WINSIZE = (Cell.width * 51, Cell.height * 51)

screen = pygame.display.set_mode(WINSIZE)
maze = Maze(WINSIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    maze.draw(screen)

    pygame.display.flip()
