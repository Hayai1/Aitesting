import pygame
class Player:
    def __init__(self):
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = pygame.Rect(100,100,5,13)
        self.player_img = pygame.image.load('assets/player.png').convert()
        self.player_img.set_colorkey((255,255,255))
        self.air_timer = 0
        self.vertical_momentum = 0
        self.movement = [0,0]
        self.moving_right = False
        self.moving_left = False

    def collision_test(self,rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list
    def move(self,tiles):
        self.movement = [0,0]
        if self.moving_right == True:
            self.movement[0] += 2
        if self.moving_left == True:
            self.movement[0] -= 2
        self.movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3

        self.rect.x += self.movement[0]
        hit_list = self.collision_test(self.rect,tiles)
        for tile in hit_list:
            if self.movement[0] > 0:
                self.rect.right = tile.left
                self.collision_types['right'] = True
            elif self.movement[0] < 0:
                self.rect.left = tile.right
                self.collision_types['left'] = True
        self.rect.y += self.movement[1]

        hit_list = self.collision_test(self.rect,tiles)
        for tile in hit_list:
            if self.movement[1] > 0:
                self.rect.bottom = tile.top
                self.collision_types['bottom'] = True
            elif self.movement[1] < 0:
                self.rect.top = tile.bottom
                self.collision_types['top'] = True
                
        if self.collision_types['bottom'] == True:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        
    def draw(self,screen,scroll):
        screen.blit(self.player_img,(self.rect.x - scroll[0],self.rect.y - scroll[1]))
    def update(self,screen,scroll,tiles):
        self.move(tiles)
        self.draw(screen,scroll)
