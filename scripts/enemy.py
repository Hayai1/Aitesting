import node
import pygame
import random
class Enemy:
    def __init__(self,x,y,startNode):
        self.x = x
        self.y = y
        self.currentNode = startNode
        self.time = 0
    def draw(self, screen,scroll):
        self.time += 1
        rndNum = random.randint(0,len(self.currentNode.connections)-1)
        if self.time % 1 == 0:
            self.currentNode = self.currentNode.connections[rndNum]
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.currentNode.x - scroll[0],self.currentNode.y - scroll[1]-16,16,16))

    
    
