import os
import csv
import pygame
import constant as const

class TileMap(pygame.sprite.Sprite):
    def __init__(self, image, x, y, wall = False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x = x, y = y)
        self.wall = wall

class World():
    def __init__(self):
        super().__init__()
        self.tile_img = self.load_tile_img()
        self.tiles = []
        self.wall = []
        
    def load_tile_img(self):
        tile_dict = {}
        scale = lambda img: pygame.transform.scale_by(img, const.TILE_FACTOR)
        for num in range(18):
            img = scale(pygame.image.load(os.path.join(const.TILE_PATH, f"{num}.png")).convert_alpha())
            tile_dict[num] = img
        return tile_dict
    
    def load_level(self, level):
        path = os.path.join(const.LEVEL_PATH, f"level{level}_data.csv")
        with open(path, "r") as file:
            csv_file = csv.reader(file, delimiter=",")
            
            for r, row in enumerate(csv_file):
                for c, col in enumerate(row):
                    id = int(col)
                    collidable = False
                    if id == const.EMPTY_TILE:
                        continue
                    if id == const.WALL_TILE:
                        collidable = True
                        
                    img = self.tile_img[id]
                    tile = TileMap(img, c * const.TILE_SIZE, r * const.TILE_SIZE, collidable)
                    self.tiles.append(tile)
                    
                    if collidable:
                        self.wall.append(tile.rect)
                        
    def load_tiles(self, screen, camera):
        offset_x, offset_y = camera.offset()
        for tile in self.tiles:
            screen.blit(tile.image, (tile.rect.x - offset_x, tile.rect.y - offset_y))