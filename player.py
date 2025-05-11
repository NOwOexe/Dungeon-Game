import pygame
import math
import constant as const
from character import *

class Player(Character):
    def __init__(self, animation, x, y, health):
        super().__init__(animation, x, y)
        self.rect = pygame.Rect(const.PLAYER_X, const.PLAYER_Y, animation[0][0].get_width(),
                                animation[0][0].get_height() - const.PLAYER_OFFSET * const.CHARACTER_FACTOR)
        self.speed = const.PLAYER_SPEED
        self.player_x, self.player_y = float(const.PLAYER_X), float(const.PLAYER_Y)
        self.health = health
        self.score = 0
        
    def draw(self, screen:pygame.Surface):
        flipped_image = pygame.transform.flip(self.image, self.is_flipped, False)
        pygame.draw.rect(screen, (const.G_COLOR), self.rect, width= 1)
        screen.blit(flipped_image, (self.rect.x, self.rect.y - const.PLAYER_OFFSET * const.CHARACTER_FACTOR))

    def move(self, dt):
        key = pygame.key.get_pressed()
        dx, dy = 0, 0
        if key[pygame.K_w]:
            dy = -self.speed
            
        if key[pygame.K_a]:
            dx = -self.speed
            self.set_flip(True)

        if key[pygame.K_s]:
            dy = self.speed

        if key[pygame.K_d]:
            dx = self.speed
            self.set_flip(False)

        if dx == 0 and dy == 0:
            self.animate = 0

        if dx != 0 or dy != 0:
            self.animate = 1

        if dx != 0 and dy != 0:
            dx *= math.cos(math.radians(45))
            dy *= math.sin(math.pi / 4)

        self.player_x += dx * dt
        self.player_y += dy * dt
        self.rect.x = int(self.player_x)
        self.rect.y = self.player_y