#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

class Barre_vie():

    #Ouverture de la fenêtre Pygame

    def __init__(self, pv, pvmax, xpos, ypos, longu, larg, c_vie, c_mort):
        super().__init__()

        self.pv = pv
        self.pvmax = pvmax
        self.xpos = xpos
        self.ypos = ypos
        self.longu = longu
        self.larg = larg
        self.long_perdu = (pvmax-pv)/pvmax*longu
        self.xpos_perdu = (xpos+longu)-self.long_perdu
        self.c_vie = c_vie
        self.c_mort = c_mort

    def barres(self, fenetre):
        WHITE=(255,255,255)
        VIE=(236, 121, 250)
        MORT=(74, 34, 141)
        if self.pv >= 0:
            pygame.draw.rect(fenetre,self.c_vie,(self.xpos,self.ypos,self.longu,self.larg))
        else:
            self.pv = 0