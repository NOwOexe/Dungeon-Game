import pygame

class Character():

    def __init__(self, image:pygame.Surface, x ,y):
        self.image = image
        self.rect = self.image.get_rect(x = x , y = y)

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect)