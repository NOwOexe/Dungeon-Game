import pygame
import math
import constant as const
from character import *

class Player(Character):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.speed = const.PLAYER_SPEED
        self.player_x, self.player_y = float(const.PLAYER_X), float(const.PLAYER_Y)

    def move(self, dt):
        key = pygame.key.get_pressed()
        dx, dy = 0, 0
        if key[pygame.K_w]:
            dy = -self.speed

        if key[pygame.K_a]:
            dx = -self.speed

        if key[pygame.K_s]:
            dy = self.speed

        if key[pygame.K_d]:
            dx = self.speed

        if dx != 0 and dy != 0:
            dx = math.cos(math.radians(45))
            dy = math.sin(math.pi / 4)

        self.player_x += dx * dt
        self.player_y += dy * dt
        self.rect.x = int(self.player_x)
        self.rect.y = int(self.player_y)