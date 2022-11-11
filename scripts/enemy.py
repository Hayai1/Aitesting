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
        self.currentNode = graph.nodes[2]
        
    def draw(self, screen,scroll):
        self.time += 1
        rndNum = random.randint(0,len(self.currentNode.connections)-1)
        if self.time % 60 == 0:
            self.currentNode = self.currentNode.connections[rndNum]
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.currentNode.x - scroll[0],self.currentNode.y - scroll[1]-16,16,16))
    def update(self,player,doAnotherPath):
        if doAnotherPath:
            self.ai.DrawPath(self.currentNode,player)

    
    
