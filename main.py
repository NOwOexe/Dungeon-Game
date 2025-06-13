import os
import pygame
import constant as const
from character import *
from player import *
from weapon import *
from enemy import *
from item import *
from world import *
from camera import *

class Damage_Text(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.start = pygame.time.get_ticks()
        self.rect = self.image.get_rect(x = x, y = y)
        self.move_up = float(self.rect.y)
        self.velocity = 1
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start
        if delta_time >= 300:
            self.kill()
        self.move_up -= self.velocity * (delta_time / 1000)
        self.rect.y = self.move_up

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
        animation = self.load_animation()
        self.player = Player(animation[self.char_dict["elf"]], const.PLAYER_X, const.PLAYER_Y, const.PLAYER_HEALTH)
        
        #Enemy
        self.enemy = Enemy(animation[self.char_dict["goblin"]], const.PLAYER_X, const.PLAYER_Y, const.ENEMY_HEALTH)
        self.enemy2 = Enemy(animation[self.char_dict["big_demon"]], const.PLAYER_X+ 100, const.PLAYER_Y, const.ENEMY_HEALTH)
        self.enemy3 = Enemy(animation[self.char_dict["skeleton"]], const.PLAYER_X +200, const.PLAYER_Y, const.ENEMY_HEALTH)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)
        self.enemy_group.add(self.enemy2)
        self.enemy_group.add(self.enemy3)

        #Arrow
        arrow_img = self.load_image(const.ARROW_PATH)
        arrow_img = self.change_scale(arrow_img, const.ARROW_FACTOR)
        self.arrow_group = pygame.sprite.Group()
        
        #Weapon
        bow_img = self.load_image(const.BOW_PATH)
        bow_img = self.change_scale(bow_img, const.BOW_FACTOR)
        self.bow = Weapon(bow_img, self.player.rect.centerx, self.player.rect.centery, arrow_img)
        
        #Damege_text_group
        self.damage_text_group = pygame.sprite.Group()
        
        #Health
        self.heart_list = []
        heart_path = ["heart_full", "heart_half", "heart_empty"]
        for i in range(3):
            heart = self.load_image(os.path.join(const.ITEM_PATH, f"{heart_path[i]}.png"))
            new_heart = self.change_scale(heart, const.HEART_FACTOR)
            self.heart_list.append(new_heart)
            
        #Coins
        self.coin_animation = self.load_coins()
        coin = Coin(self.coin_animation[0], self.coin_animation, 500, 500)
        self.coin_group = pygame.sprite.Group()
        self.coin_group.add(coin)
        
        #Potion
        potion_img = self.change_scale(self.load_image(os.path.join(const.ITEM_PATH, "potion_red.png")), const.POTION_FACTOR)
        potion = Potion(potion_img, 100, 100)
        self.potion_group = pygame.sprite.Group()
        self.potion_group.add(potion)
        
        #Font
        self.score_font = pygame.font.Font(const.FONT_PATH, 24)
        
        #Map
        # self.map_dict = {
        #     0: self.change_scale(self.load_image(os.path.join(const.TILE_PATH, "0.png")), const.TILE_FACTOR),
        #     7: self.change_scale(self.load_image(os.path.join(const.TILE_PATH, "7.png")), const.TILE_FACTOR)
        # }
        
        # self.map = [
        #     [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 0, 7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 7, 7, 7],
        #     [7, 7, 0, 7, 0, 7, 7, 7, 7, 0, 7, 7, 0, 7, 7, 7],
        #     [7, 7, 0, 7, 0, 7, 7, 7, 7, 0, 0, 0, 0, 7, 7, 7],
        #     [7, 7, 0, 7, 0, 7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 0, 0, 0, 7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 0, 7, 0, 0, 0, 7, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 0, 0, 0, 7, 0, 0, 0, 7, 7, 7, 7, 7],
        #     [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        # ]
        
        self.world = World()
        self.world.load_level(1)
        
        #Camera
        self.camera = Camera()
                
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
    
    def load_coins(self):
        coin_animation = []
        for i in range(4):
            coin = self.load_image(os.path.join(const.ITEM_PATH, f"coin_f{i}.png"))
            new_coin = self.change_scale(coin, const.COIN_FACTOR)
            coin_animation.append(new_coin)
        return coin_animation
    
    def display_health(self):
        pygame.draw.rect(self.screen, (const.GR_COLOR), (0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT / 10))
        half_heart = False
        for i in range(5):
            if self.player.health >= (i + 1) * 20:
                self.screen.blit(self.heart_list[0], (10 + (i * 35), 10))
            elif self.player.health % 20 > 0 and not half_heart:
                self.screen.blit(self.heart_list[1], (10 + (i * 35), 10))
                half_heart = True
            else:
                self.screen.blit(self.heart_list[2], (10 + (i * 35), 10))
                
    def display_score(self):
        score = self.score_font.render(f"x{str(self.player.score)}", True, const.W_COLOR)
        self.screen.blit(score, (const.SCREEN_WIDTH - 60, 15))
        self.screen.blit(self.coin_animation[0], (const.SCREEN_WIDTH - 90, 15))
        
    # def load_map(self):
    #     for r, row in enumerate(self.map):
    #         for c, col in enumerate(row):
    #             self.screen.blit(self.map_dict[col], (const.TILE_SIZE * c, const.TILE_SIZE * r))

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
            # self.load_map()
            self.world.load_tiles(self.screen, self.camera)
            self.display_health()
            self.player.draw(self.screen, self.camera)
            self.player.move(delta_time)
            self.bow.draw(self.screen, self.camera)
            self.player.update()
            self.arrow = self.bow.update(self.player, self.camera)
            if self.arrow:
                self.arrow_group.add(self.arrow)
            self.arrow_group.draw(self.screen)
            self.arrow_group.update(delta_time, self.enemy_group, self.damage_text_group)
            self.enemy_group.draw(self.screen)
            self.damage_text_group.draw(self.screen)
            self.damage_text_group.update()
            self.coin_group.draw(self.screen)
            self.coin_group.update()
            self.potion_group.draw(self.screen)
            self.display_score()
            for coin in self.coin_group:
                coin.check_collide(self.player)
            for potion in self.potion_group:
                potion.heal(self.player)
            self.camera.update(self.player.rect)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()