import pygame
from character import *

class Enemy(Character):
    
    def __init__(self, animation, x, y, health):
        super().__init__(animation, x, y)
        self.speed = None
        self.health = health
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def update(self):
        pass