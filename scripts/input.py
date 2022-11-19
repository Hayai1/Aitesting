import pygame,sys
from pygame.locals import *
class Input:
    def __init__(self,player):
        self.player = player
    def update(self):
        DoAnotherPath = False
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.moving_right = True
                if event.key == K_LEFT:
                    self.player.moving_left = True
                if event.key == K_UP:
                    if self.player.air_timer < 6:
                        self.player.vertical_momentum = -5                
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.moving_right = False
                if event.key == K_LEFT:
                    self.player.moving_left = False
    