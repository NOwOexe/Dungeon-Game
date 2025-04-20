import pygame
import math
from player import *

class Weapon():
    def __init__(self, img, x, y, arrow_img):
        self.original_image = img
        self.bow_angle = 0
        self.arrow_img = arrow_img
        self.rect = pygame.Rect(x, y, img.get_width(), img.get_height())
        self.rotated_image = pygame.transform.rotate(self.original_image, self.bow_angle)
        self.start_time = pygame.time.get_ticks()
        self.is_fired = False

    def draw(self, screen):
        self.rect = self.rotated_image.get_rect(center = self.rect.center)
        screen.blit(self.rotated_image, self.rect)

    def update(self, player:Player):
        cursor_pos = pygame.mouse.get_pos()
        self.rect.center = player.rect.center
        dx = cursor_pos[0] - self.rect.centerx
        dy = -(cursor_pos[1] - self.rect.centery)
        self.bow_angle = math.degrees(math.atan2(dy, dx))
        self.rotated_image = pygame.transform.rotate(self.original_image, self.bow_angle)
        
        #Arrow
        arrow = None
        if pygame.mouse.get_pressed()[0] and not self.is_fired:
            self.is_fired = True
            arrow = Arrow(player.rect.centerx, player.rect.centery, self.bow_angle, self.arrow_img)
            self.start_time = pygame.time.get_ticks()
                
        if not pygame.mouse.get_pressed()[0] and self.is_fired:
            current_time = pygame.time.get_ticks()
            delta_time = current_time - self.start_time
            if delta_time >= const.ARROW_RELOAD:
                self.is_fired = False
                self.start_time = current_time
        return arrow
        
        
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, image:pygame.surface):
        super().__init__()
        self.original_image = image
        self.angle = angle
        self.speed = 200
        self.arrow_x = float(x)
        self.arrow_y = float(y)
        self.rect = image.get_rect(centerx = x, centery = y)
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90) #This is rotated image
        
    def update(self, delta_time):
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))
        self.arrow_x += dx * self.speed * delta_time
        self.arrow_y += -(dy * self.speed * delta_time)
        self.rect.x = int(self.arrow_x)
        self.rect.y = int(self.arrow_y)