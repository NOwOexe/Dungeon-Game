import os
import pygame
import constant as const
from character import *
from player import *
from weapon import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dungeon Game")
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.start_time = pygame.time.get_ticks()
        self.char_dict = {
            "elf" : 0,
            "big_demon" : 1,
            "goblin" : 2,
            "imp" : 3,
            "muddy" : 4,
            "skeleton" : 5,
            "tiny_zombie" : 6
        }

        #Player
        player_idle_animation = self.load_animation()
        self.player = Player(player_idle_animation[self.char_dict["elf"]], const.PLAYER_X, const.PLAYER_Y)

        #Weapon
        bow_img = self.load_image(const.BOW_PATH)
        bow_img = self.change_scale(bow_img, const.BOW_FACTOR)
        self.bow = Weapon(bow_img, self.player.rect.x, self.player.rect.y)
 
    def change_scale(self, image, factor):
        image = pygame.transform.scale_by(image, factor)
        return image
    
    def load_image(self, path):
        return pygame.image.load(path).convert_alpha()
    
    def load_animation(self):
        char_lst = ["elf", "big_demon", "goblin", "imp", "muddy", "skeleton", "tiny_zombie"]
        idle_run_lst = []
        lst = ["idle", "run"]
        for char in char_lst:
            temp_lst = []
            for animate in lst:
                temp_lst_2 = []
                for i in range(4):
                    image = self.load_image(os.path.join(const.PLAYER_PATH, f"{char}/{animate}/{i}.png"))
                    image = self.change_scale(image, const.CHARACTER_FACTOR)
                    temp_lst_2.append(image)
                temp_lst.append(temp_lst_2)
            idle_run_lst.append(temp_lst)
        return idle_run_lst

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
            self.bow.draw(self.screen)
            self.player.update()
            self.bow.update(self.player)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()