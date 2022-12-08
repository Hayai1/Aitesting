import pygame
from player import Player
from enemy import Enemy
from camera import Camera
from input import Input
from world import World
from screen import Screen
from pygame.locals import *

pygame.init() # initiates pygame

screen = Screen((600,400),"PlaceHolder",60)
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
world = World('data/map')
player1 = Player(100,100,5,13,'assets/player.png',2)
enemy1 = Enemy(world.worldGraph.nodes[10].x,world.worldGraph.nodes[10].y-13,5,13,world.worldGraph,'assets/enemy.png',1)
camera = Camera(player1)
input = Input(player1)

while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue
    enemy1.update(player1)
    camera.update()
    input.update(enemy1)
    enemy1.draw(display,camera.scroll,world.tile_rects)
    player1.update(display,camera.scroll,world.tile_rects)
    world.draw(display,camera.scroll)
    screen.update(display)
