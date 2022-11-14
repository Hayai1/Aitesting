import pygame
from player import Player
from graph import Graph
from enemy import Enemy
from camera import Camera
from input import Input
from world import World
from screen import Screen
from pygame.locals import *

pygame.init() # initiates pygame

screen = Screen((600,400),"Platformer",60)
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
world = World('data/map')
graph = Graph(world.map)
player1 = Player()
enemy1 = Enemy(100,100,graph)
camera = Camera(player1)
input = Input(player1)

doAnotherPath = False
while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue
    enemy1.update(player1,doAnotherPath)
    camera.update()
    doAnotherPath = input.update()
    enemy1.draw(display,camera.scroll)
    player1.update(display,camera.scroll,world.tile_rects)
    world.draw(display,camera.scroll)
    graph.draw(display,camera.scroll)
    screen.update(display)

#TODO:
'''
test the node generation and connections in differnt map styles 

then when happy with node generation make the enemy walk to each node and posibly fall/jump to next node if needed
'''