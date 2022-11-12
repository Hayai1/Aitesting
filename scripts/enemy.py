import pygame
from ai import Ai
class Enemy:
    def __init__(self,x,y,graph):
        self.x = x
        self.y = y
        self.time = 0
        self.ai = Ai(graph)
        self.currentNode = graph.nodes[2]
        self.counter = 0
        self.path = None
    def draw(self, screen,scroll):
        self.time += 1
        
        if self.path != None:
            if self.time % 15 == 0:
                self.currentNode = self.path[self.counter]
                self.counter += 1
            if len(self.path) == self.counter:
                self.counter = 0
                self.path = None
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.currentNode.x - scroll[0],self.currentNode.y - scroll[1]-16,16,16))
    def update(self,player,doAnotherPath):
        if doAnotherPath:
            self.path = self.ai.DrawPath(self.currentNode,player)
            self.counter = 0

    
    
