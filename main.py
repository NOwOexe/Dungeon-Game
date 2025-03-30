import os
import pygame
import constant as const
from character import *
from player import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dungeon Game")
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.start_time = pygame.time.get_ticks()

        #Player
        player_idle_animation = self.load_animation()
        self.player = Player(player_idle_animation, const.PLAYER_X, const.PLAYER_Y)

    def change_scale(self, image):
        image = pygame.transform.scale_by(image, const.CHARACTER_FACTOR)
        return image
    
    def load_image(self, path):
        return pygame.image.load(path).convert_alpha()
    
    def load_animation(self):
        lst = []
        for i in range(4):
            image = self.load_image(os.path.join(const.PLAYER_PATH, f"{i}.png"))
            image = self.change_scale(image)
            lst.append(image)
        return lst

    def run(self):
        run = True
        while run:
            current_time = pygame.time.get_ticks()
            delta_time = (current_time - self.start_time) / 1000.0
            self.start_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill(const.BACKGROUND_COLOR)
            self.player.draw(self.screen)
            self.player.move(delta_time)
            self.player.update()
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()