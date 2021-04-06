import pygame

from pygame.locals import (
    K_r,
    K_q,
    K_d,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

from lib.cell import Cell
from lib.maze import Maze
from lib.astar import Astar


WINSIZE = (Cell.width * 51, Cell.height * 51)


def draw_maze(maze):
    maze.draw()
    maze.generate()


def set_sleep(n, maze, astar):
    if n == 0:
        maze.sleep = 1
        astar.sleep = 1
    elif not (n < 0 and maze.sleep < 10):
        maze.sleep += n
        astar.sleep += n
    draw_maze(maze)


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINSIZE)
    clock = pygame.time.Clock()

    maze = Maze(
        WINSIZE,
        diagonal=False,
        screen=screen,
        animate=True,
        sleep=1
    )
    astar = Astar(
        maze,
        screen=screen,
        animate=True,
        sleep=1
    )

    draw_maze(maze)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_r:
                    set_sleep(0, maze, astar)

                if event.key == K_d:
                    maze.diagonal = False if maze.diagonal else True
                    draw_maze(maze)

                if event.unicode == '+':
                    set_sleep(10, maze, astar)

                if event.unicode == '-':
                    set_sleep(-10, maze, astar)

                if event.key == K_SPACE:
                    astar.search()

                elif event.key == K_q:
                    running = False

            elif event.type == QUIT:
                running = False

        pygame.display.flip()
        clock.tick()


if __name__ == '__main__':
    main()
