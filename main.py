import pygame

from pygame.locals import QUIT

from lib.cell import Cell
from lib.maze import Maze

pygame.init()

WINSIZE = (Cell.width * 51, Cell.height * 51)

screen = pygame.display.set_mode(WINSIZE)
clock = pygame.time.Clock()

maze = Maze(WINSIZE)
maze.draw(screen)
maze.generate(screen, True, 1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()
    clock.tick()
