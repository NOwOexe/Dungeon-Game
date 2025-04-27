import pygame
import constant as const

class Character(pygame.sprite.Sprite):

    def __init__(self, animation:pygame.Surface, x ,y):
        super().__init__()
        self.image = animation[0][0]
        self.animation = animation
        self.rect = self.image.get_rect(x = x , y = y)
        self.cur_animation = 0
        self.start_time = pygame.time.get_ticks()
        self.is_flipped = False
        self.animate = 0

    def draw(self, screen:pygame.Surface):
        flipped_image = pygame.transform.flip(self.image, self.is_flipped, False)
        pygame.draw.rect(screen, (const.G_COLOR), self.rect, width= 1)
        screen.blit(flipped_image, self.rect)
        
    def set_flip(self, is_flipped):
        self.is_flipped = is_flipped
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start_time
        if delta_time > const.ANIMATION_COOLDOWN:
            if self.cur_animation >= len(self.animation[0]):
                self.cur_animation = 0
            self.image = self.animation[self.animate][self.cur_animation]
            self.cur_animation += 1
            self.start_time = current_time