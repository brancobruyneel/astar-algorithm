import pygame

from pygame.locals import QUIT

from lib.cell import Cell

pygame.init()

WINSIZE = (Cell.w * 101, Cell.h * 51)

screen = pygame.display.set_mode(WINSIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()
