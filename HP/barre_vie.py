#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

class Barre_vie():

    def __init__(self, hp, hpmax, xpos, ypos, longu, larg, c_vie, c_mort):
        super().__init__()

        self.hp = hp # number of hp left
        self.hpmax = hpmax # maximum nb of hp, 100 by default
        self.xpos = xpos # x position of life bar
        self.ypos = ypos # y position of life bar
        self.longu = longu # length
        self.larg = larg # width
        self.long_perdu = (self.hpmax-self.hp)/self.hpmax*self.longu # lost length on bar
        self.xpos_perdu = (self.xpos+self.longu)-self.long_perdu # lost length on x axis for left of bar
        self.c_vie = c_vie # color for life left
        self.c_mort = c_mort # color for life lost

    def barres(self, screen):
        if self.hp >= 0:
            pygame.draw.rect(screen,self.c_vie,(self.xpos,self.ypos,self.longu,self.larg))
            pygame.draw.rect(screen,self.c_mort,(self.xpos_perdu,self.ypos,self.long_perdu,self.larg))
        else:
            self.hp = 0