#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

class Barre_vie():

    def __init__(self, hp, hpmax, xpos, ypos, longu, larg, c_vie, c_mort):
        super().__init__()

        self.hp = hp
        self.hpmax = hpmax
        self.xpos = xpos
        self.ypos = ypos
        self.longu = longu
        self.larg = larg
        self.long_perdu = (self.hpmax-self.hp)/self.hpmax*self.longu
        self.xpos_perdu = (self.xpos+self.longu)-self.long_perdu
        self.c_vie = c_vie
        self.c_mort = c_mort

    def barres(self, screen):
        WHITE=(255,255,255)
        VIE=(236, 121, 250)
        MORT=(74, 34, 141)
        if self.hp >= 0:
            pygame.draw.rect(screen,self.c_vie,(self.xpos,self.ypos,self.longu,self.larg))
            pygame.draw.rect(screen,self.c_mort,(self.xpos_perdu,self.ypos,self.long_perdu,self.larg))
        else:
            self.hp = 0