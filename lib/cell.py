import pygame


class Cell(pygame.sprite.Sprite):
    width = 16
    height = 16

    def __init__(self, x, y):
        super(Cell, self).__init__()

        self.surf = pygame.Surface([self.width, self.height])
        self.surf.fill((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = x * self.width
        self.rect.y = y * self.width

        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
