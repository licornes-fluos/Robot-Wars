#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

class Barre_vie():

    #Ouverture de la fenêtre Pygame

    def __init__(self, pv, pvmax, xpos, ypos, longu, larg):
        super().__init__()

        self.pv = pv
        self.pvmax = pvmax
        self.xpos = xpos
        self.ypos = ypos
        self.longu = longu
        self.larg = larg
        self.long_perdu=(pvmax-pv)/pvmax*longu
        self.xpos_perdu=(xpos+longu)-self.long_perdu

    def barres(self, fenetre):
        WHITE=(255,255,255)
        VIE=(236, 121, 250)
        MORT=(74, 34, 141)
        pygame.draw.rect(fenetre,VIE,(self.xpos,self.ypos,self.longu,self.larg))
        pygame.draw.rect(fenetre,MORT,(self.xpos_perdu,self.ypos,self.long_perdu,self.larg))
