import pygame
import constant as const

class TileMap(pygame.sprite.Sprite):
    def __init__(self, image, x, y, wall = False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x = x, y = y)
        self.wall = wall

class World(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = []
        self.wall = []