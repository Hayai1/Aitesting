import pygame,sys
from pygame.locals import *
class Input:
    def __init__(self,player):
        self.player = player
    def update(self):
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.movingRight = True
                if event.key == K_LEFT:
                    self.player.movingLeft = True
                if event.key == K_UP:
                    if self.player.air_timer < 6:
                        self.player.verticalAcceleration = -5                
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.movingRight = False
                if event.key == K_LEFT:
                    self.player.movingLeft = False
    