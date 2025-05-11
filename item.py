import pygame
import constant as const

class Item(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x = x, y = y)
            
class Coin(Item):
    def __init__(self, image, animation, x, y):
        super().__init__(image, x, y)
        self.animation = animation
        self.cur_frame = 0
        self.start = pygame.time.get_ticks()
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start
        if delta_time > const.ANIMATION_COOLDOWN:
            if self.cur_frame >= len(self.animation):
                self.cur_frame = 0
            self.image = self.animation[self.cur_frame]
            self.cur_frame += 1
            self.start = current_time
            
    def check_collide(self, player):
        if self.rect.colliderect(player.rect):
            player.score += 1
            self.kill()
            
class Potion(Item):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        
    def heal(self, player):
        if self.rect.colliderect(player.rect):
            player.health += 20
            self.kill()