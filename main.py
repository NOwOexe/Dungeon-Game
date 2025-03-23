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
        player_image  = pygame.image.load(const.PLAYER_PATH).convert_alpha()
        player_image = self.change_scale(player_image)
        self.player = Player(player_image, const.PLAYER_X, const.PLAYER_Y)

    def change_scale(self, image):
        image = pygame.transform.scale_by(image, const.CHARACTER_FACTOR)
        return image

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
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()