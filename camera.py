import constant as const

class Camera():
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        
    def update(self, player_rect):
        self.offset_x = player_rect.centerx - const.SCREEN_WIDTH // 2
        self.offset_y = player_rect.centery - const.SCREEN_HEIGHT // 2
        
    def offset(self):
        return self.offset_x, self.offset_y