import pygame
import math
from player import *

class Weapon():
    def __init__(self, img, x, y):
        self.image = img
        self.bow_angle = 0
        self.rect = pygame.Rect(x, y, img.get_width(), img.get_height())

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, player:Player):
        dx, dy = 0, 0
        cursor_pos = pygame.mouse.get_pos()
        self.rect.center = player.rect.center
        dx = cursor_pos[0] - self.rect.centerx
        dy = -(cursor_pos[1] - self.rect.centery)
        self.bow_angle = math.atan2(dy, dx)