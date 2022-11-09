import pygame, sys, json
from player import Player
from node import Node
from enemy import Enemy
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() # initiates pygame

pygame.display.set_caption('Pygame Platformer')

WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

true_scroll = [0,0]

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('data/map')
mapConnections = load_map('data/mapConnections')
grass_img = pygame.image.load('assets/grass.png')
dirt_img = pygame.image.load('assets/dirt.png')


tile_rects = []

def openJsonFile():
    with open('data/mapNodeLayout.json') as f:
        data = json.load(f)['nodes']
        nodes = []
        nodeDictAndConnections = {}
        for node in data:
            nodeData = data[node]
            id = nodeData['id']
            x = nodeData['x']
            y = nodeData['y']
            newNode = Node(id,x*16,y*16)
            nodes.append(newNode)
            nodeDictAndConnections[node] = [newNode,[]]
            for connection in nodeData['connections']:
                nodeDictAndConnections[node][1].append(connection)
            
        for node in nodeDictAndConnections:
            for connection in nodeDictAndConnections[node][1]:
                parentNode = nodeDictAndConnections[node][0]
                parentNode.add_connection(nodeDictAndConnections[connection['id']][0])
    return nodes

nodes = openJsonFile()
player1 = Player()
enemy1 = Enemy(100,100,nodes[1])



while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue

    true_scroll[0] += (player1.rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player1.rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    
    
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            if (int(tile) % 2) == 0 and tile != '0':
                display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
            elif tile != '0':
                display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
            
            x += 1
        y += 1

    for node in nodes:
        coords = [[node.x-scroll[0],node.y-scroll[1]]]
        for connection in node.connections:
            coords.append([connection.x-scroll[0],connection.y-scroll[1]])
        if len(coords) >= 2:
            coords = sorted(coords)
            pygame.draw.lines(display,(255,0,0),False,coords,1)
        coords = []

    enemy1.draw(display,scroll)
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player1.moving_right = True
            if event.key == K_LEFT:
                player1.moving_left = True
            if event.key == K_UP:
                if player1.air_timer < 6:
                    player1.vertical_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player1.moving_right = False
            if event.key == K_LEFT:
                player1.moving_left = False
    player1.update(display,scroll,tile_rects)
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
