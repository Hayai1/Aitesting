import pygame
from character import Character
class Player(Character):
    def __init__(self, x, y, width, height,imgPath,xvel=1):
        super().__init__(x, y, width, height,imgPath,xvel)  
    def draw(self,screen,scroll):
        screen.blit(self.img,(self.rect.x - scroll[0],self.rect.y - scroll[1]))
    def update(self,screen,scroll,tiles):
        self.move(tiles)
        self.draw(screen,scroll)
