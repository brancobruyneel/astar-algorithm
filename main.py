import pygame

from pygame.locals import QUIT

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400


class Cell(pygame.sprite.Sprite):
    width = 16
    height = 16

    def __init__(self, x, y):
        super(Cell, self).__init__()

        self.surf = pygame.Surface([self.width, self.height])
        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()
        self.rect.x = x * self.width
        self.rect.y = y * self.width

        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


cell = Cell(0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    cell.draw(screen)

    pygame.display.flip()
