import pygame
from physics import CharacterPhysics
class Character:
    def __init__(self,x,y,width,height,imgPath,xVelocity):
        self.rect = pygame.Rect(x,y,width,height)
        self.img = pygame.image.load(imgPath).convert()
        self.img.set_colorkey((255,255,255))
        self.phyiscs = CharacterPhysics()
        self.verticalAcceleration = 0
        self.air_timer = 0
        self.xVelocity = xVelocity
        self.movingRight = False
        self.movingLeft = False
        self.movement = [0,0]
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    @property
    def x(self):
        return self.rect.x
    @x.setter
    def x(self, value):
        self.rect.x = value
    @property
    def y(self):
        return self.rect.y
    @y.setter
    def y(self, value):
        self.rect.y = value
    def move(self,tiles):
        self.movement = [0,0]
        if self.movingRight:#moving right
            self.movement[0] += self.xVelocity
        if self.movingLeft:#moving left
            self.movement[0] -= self.xVelocity
        self.movement[1] += self.verticalAcceleration
        self.verticalAcceleration += 0.2
        if self.verticalAcceleration > 3:
            self.verticalAcceleration = 3

        self.rect.x += self.movement[0]
        hit_list = self.phyiscs.collision_test(self.rect,tiles)
        for tile in hit_list:
            if self.movement[0] > 0:
                self.rect.right = tile.left
                self.collision_types['right'] = True
            elif self.movement[0] < 0:
                self.rect.left = tile.right
                self.collision_types['left'] = True
        
        self.rect.y += self.movement[1]

        hit_list = self.phyiscs.collision_test(self.rect,tiles)
        for tile in hit_list:
            if self.movement[1] > 0:
                self.rect.bottom = tile.top
                self.collision_types['bottom'] = True
            elif self.movement[1] < 0:
                self.rect.top = tile.bottom
                self.collision_types['top'] = True
             
        if self.collision_types['bottom'] == True:
            self.air_timer = 0
            self.verticalAcceleration = 0
        else:
            self.air_timer += 1
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        
        
  