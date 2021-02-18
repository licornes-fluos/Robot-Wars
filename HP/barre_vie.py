#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

class Barre_vie():
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((1920,1080))
    WHITE=(255,255,255)
    VIE=(236, 121, 250)
    MORT=(74, 34, 141)
    def __init__(self, pv, pvmax, xpos, ypos, longu, larg):
        super().__init__()

        self.pv = pv
        self.pvmax = pvmax
        self.xpos = xpos
        self.ypos = ypos
        self.longu = longu
        self.larg = larg
        self.long_perdu=(pvmax-pv)/pvmax*longu
        self.xpos_perdu=(xpos+longu)-long_perdu
        self.pygame.draw.rect(fenetre,VIE,(xpos,ypos,longu,larg))
        self.pygame.draw.rect(fenetre,MORT,(xpos_perdu,ypos,long_perdu,larg))

    def barres(self, pv, pvmax, xpos, ypos, longu, larg):

        #BOUCLE INFINIE
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()