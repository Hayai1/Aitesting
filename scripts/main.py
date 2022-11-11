import pygame
import random
from player import Player
from graph import Graph
from enemy import Enemy
from camera import Camera
from input import Input
from world import World
from screen import Screen
from ai import Ai
from pygame.locals import *

pygame.init() # initiates pygame

screen = Screen((600,400),"Platformer",60)
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
graph = Graph('data/mapNodeLayout.json')
player1 = Player()
currentNode = graph.nodes[1]
enemy1 = Enemy(100,100,graph)

camera = Camera(player1)
input = Input(player1)
world = World('data/map')
ai = Ai(graph)
n = 16
path = ai.findPath(graph.nodes[0],graph.nodes[n])
graph.nodes[n].color = (0,255,0)
for node in path:
    node.color = (0,0,255)
time = 0

while True: # game loop
    time += 1
    if time % 120 == 0:
        for nodes in graph.nodes:
            nodes.color = (255,255,0)
        n = random.randint(0,len(graph.nodes)-1)
        path = ai.findPath(graph.nodes[0],graph.nodes[n])
        graph.nodes[n].color = (0,255,0)
        for node in path:
            node.color = (0,0,255)
    display.fill((146,244,255)) # clear screen by filling it with blue
    camera.update()
    input.update()
    currentNode = enemy1.draw(display,camera.scroll,currentNode)
    player1.update(display,camera.scroll,world.tile_rects)
    world.draw(display,camera.scroll)
    graph.draw(display,camera.scroll)
    #graph.getNodeCloseToPlayer(player1)
    screen.update(display)