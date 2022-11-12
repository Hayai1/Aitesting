import pygame
import random
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
graph = Graph('data/mapNodeLayout.json')
player1 = Player()
enemy1 = Enemy(100,100,graph)
camera = Camera(player1)
input = Input(player1)
world = World('data/map')

doAnotherPath = False
while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue
    enemy1.update(player1,doAnotherPath)
    camera.update()
    doAnotherPath = input.update()
    enemy1.draw(display,camera.scroll)
    player1.update(display,camera.scroll,world.tile_rects)
    world.draw(display,camera.scroll)
    graph.nodes[9].color = (0,255,0)
    graph.draw(display,camera.scroll)
    screen.update(display)