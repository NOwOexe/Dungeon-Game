import pygame
import constant as const

class Items(pygame.sprite.Sprite):
    def __init__(self, image, animation, x, y):
        super().__init__()
        self.image = image
        self.animation = animation
        self.cur_frame = 0
        self.start = pygame.time.get_ticks()
        self.rect = self.image.get_rect(x = x, y = y)
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start
        if delta_time > const.ANIMATION_COOLDOWN:
            if self.cur_frame >= len(self.animation):
                self.cur_frame = 0
            self.image = self.animation[self.cur_frame]
            self.cur_frame += 1
            self.start = current_time