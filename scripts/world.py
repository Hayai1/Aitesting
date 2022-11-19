import pygame
from graph import Graph
class World:
    def __init__(self,worldPath):
        self.map = self.load_map(worldPath)
        self.grass_img = pygame.image.load('assets/grass.png')
        self.dirt_img = pygame.image.load('assets/dirt.png')
        self.tile_rects = []
        self.worldGraph = Graph(self.map) # Create a graph
        
    def load_map(self,path):
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map
        
    def draw(self,screen,scroll):
        self.tile_rects = []
        y = 0
        for layer in self.map:
            x = 0
            for tile in layer:
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == '2':
                    screen.blit(self.grass_img,(x*16-scroll[0],y*16-scroll[1]))
                elif tile == '1':
                    screen.blit(self.dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                x += 1
            y += 1
        self.worldGraph.draw(screen,scroll)