import pygame
from ai import Ai
import random
class Enemy:
    def __init__(self,x,y,graph):
        self.img = pygame.image.load('assets/enemy.png').convert()
        self.img.set_colorkey((255,255,255))
        self.currentNode = graph.nodes[10]
        self.x = graph.nodes[10].x
        self.y = graph.nodes[10].y
        self.rect = pygame.Rect(self.x-5,self.y-13,5,13)
        self.time = 0
        self.air_timer = 0
        self.vertical_momentum = 0
        self.ai = Ai(graph)
        self.counter = 0
        self.path = None
        self.frame = 0
        self.moving = False
        self.nextNode = None
        self.movingRight = False
        self.movingLeft = False
    def draw(self, screen,scroll,tiles):
        self.movingLeft = False
        self.movingRight = False
        if self.path is not None:
            if self.counter < len(self.path):
                self.nextNode = self.path[self.counter]
                if self.currentNode.getG(self.nextNode) == 0:
                    if self.nextNode < self.currentNode:
                        self.movingLeft = True
                        self.movingRight = False
                    elif self.nextNode > self.currentNode:
                        self.movingRight = True
                        self.movingLeft = False
                else:
                    self.x = self.nextNode.x
                    self.y = self.nextNode.y
        
        self.move(tiles)
        screen.blit(self.img, (self.x - scroll[0]-5,self.y - scroll[1]-13))
        '''
        if self.path != None:
            if self.currentNode.getG(self.path[self.counter]) == 0:
                #atNextNode=self.move(self.currentNode, self.path[self.counter])
                atNextNode=self.moveTooNextNode(self.currentNode, self.path[self.counter],tiles)
            else:
                atNextNode = True
                #self.jump()
                self.x = self.path[self.counter].x
                self.y = self.path[self.counter].y
            if atNextNode:
                self.currentNode = self.path[self.counter]
                self.counter +=1     
            if len(self.path) == self.counter:
                self.counter = 0
                self.path = None
        #pygame.draw.rect(screen,(0,255,0),pygame.Rect(self.x - scroll[0]-8,self.y - scroll[1]-16,16,16))
        screen.blit(self.img, (self.rect.x - scroll[0],self.rect.y - scroll[1]))
        #screen.blit(self.img, (self.x - scroll[0]-5,self.y - scroll[1]-13))
   '''
    def update(self,player,doAnotherPath):
        if doAnotherPath:
            self.path = self.ai.DrawPath(self.currentNode,player)
            self.counter = 0
            self.nextNode = None
    
            
    def move2(self,node,connection):
        if connection is None or node is None:
            return False
        if node.x < connection.x:
            self.x += 1
        if node.x > connection.x:
            self.x -= 1
        self.frame += 1
        if self.frame == 16:
            self.frame = 0
            self.currentNode = self.nextNode
            return True
        return False
    
    def collision_test(self,rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list
    def jump(self):
        if self.air_timer < 6:
            self.vertical_momentum = -5
    def move(self,tiles):
        self.jump()
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        movement = [0,0]
        if self.movingRight:#moving right
            movement[0] += 1
        if self.movingLeft:#moving left
            movement[0] -= 1
        movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3

        self.rect.x += movement[0]
        hit_list = self.collision_test(self.rect,tiles)
        for tile in hit_list:
            if movement[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True
        
        self.rect.y += movement[1]

        hit_list = self.collision_test(self.rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
             
        if collision_types['bottom'] == True:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
        
        
        
    
    

        
        
        
    
    
