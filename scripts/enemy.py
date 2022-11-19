import pygame
from ai import Ai
from character import Character
class Enemy(Character):
    def __init__(self,x, y, width, height,graph,imgPath,xVelocity=1):
        self.graph = graph
        self.ai = Ai(graph)
        self.currentNode = graph.nodes[10]
        self.time = 4
        self.counter = 1
        self.frame = 1
        self.path = None
        self.nextNode = None
        super().__init__(x, y, width, height,imgPath,xVelocity)
        
    def draw(self, screen,scroll,tiles):
        self.movingLeft = False
        self.movingRight = False
        if self.path is not None:
            self.frame += 1
            if self.frame == 16:
                self.frame = 0
                self.currentNode = self.nextNode
                self.counter += 1
            if self.counter < len(self.path):
                self.nextNode = self.path[self.counter]
                if self.currentNode is not None:
                    if self.currentNode.getG(self.nextNode) is not 0 and self.nextNode.y < self.currentNode.y:
                        self.jump()
                    if self.nextNode.x > self.currentNode.x:
                        self.movingLeft = False
                        self.movingRight = True
                    elif self.nextNode.x < self.currentNode.x:
                        self.movingRight = False
                        self.movingLeft = True
            else:
                self.time += 1
                node = self.graph.getNodeCloseTo(self)
                if node.x > self.rect.x:
                    self.movingLeft = False
                    self.movingRight = True
                elif node.x < self.rect.x:
                    self.movingRight = False
                    self.movingLeft = True

        self.move(tiles)
        screen.blit(self.img, (self.rect.x - scroll[0],self.rect.y - scroll[1]))
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
    def update(self,player):
        if self.time >= 1 and self.graph.getNodeCloseTo(self) is not self.graph.getNodeCloseTo(player):
            self.path = self.ai.DrawPath(self.graph.getNodeCloseTo(self),player)
            self.counter = 1
            self.time = 0
            self.frame = 0
            self.nextNode = None
    
    def collision_test(self,rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list
    def jump(self):
        if self.air_timer < 6:
            self.verticalAcceleration = -5
    def move(self,tiles):
        
        self.movement = [0,0]
        if self.movingRight:#moving right
            self.movement[0] += 1
        if self.movingLeft:#moving left
            self.movement[0] -= 1
        self.movement[1] += self.verticalAcceleration
        self.verticalAcceleration += 0.2
        if self.verticalAcceleration > 3:
            self.verticalAcceleration = 3

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
            self.verticalAcceleration = 0
        else:
            self.air_timer += 1
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        
        
        
    
    

        
        
        
    
    
