import node
import pygame
import random
from ai import Ai
class Enemy:
    def __init__(self,x,y,graph):
        self.x = x
        self.y = y
        self.time = 0
        self.ai = Ai(graph)
        
    def draw(self, screen,scroll,currentNode):
        self.time += 1
        rndNum = random.randint(0,len(currentNode.connections)-1)
        if self.time % 60 == 0:
            currentNode = currentNode.connections[rndNum]
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(currentNode.x - scroll[0],currentNode.y - scroll[1]-16,16,16))
        return currentNode
    def update(self,player,doAnotherPath):
        if doAnotherPath:
            self.ai.DrawARandomPath(player)

    
    
