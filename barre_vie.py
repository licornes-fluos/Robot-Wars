#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1920,1080))
WHITE=(255,255,255)
VIE=(236, 121, 250)
MORT=(74, 34, 141)

#Chargement et collage du fond
fond = pygame.image.load("assets/bg3.png").convert()
fenetre.blit(fond, (0,0))
Pv_P1=100 # variable qui diminuera quand touché par une bombe
Pvmax=100
Xpos_P1=330
Ypos_P1=110
LongBarVie=495
LargBarVie=75
LongBarViePerdu_P1=(Pvmax-Pv_P1)/Pvmax*LongBarVie
XposBarViePerdu_P1=(Xpos_P1+LongBarVie)-LongBarViePerdu_P1
pygame.draw.rect(fenetre,VIE,(Xpos_P1,Ypos_P1,LongBarVie,LargBarVie))
pygame.draw.rect(fenetre,MORT,(XposBarViePerdu_P1,Ypos_P1,LongBarViePerdu_P1,LargBarVie))

# idem pour le deuxième joueur
Pv_P2=100
Pvmax=100
Xpos_P2=1105
Ypos_P2=110
LongBarVie=495
LargBarVie=75
LongBarViePerdu_P2=(Pvmax-Pv_P2)/Pvmax*LongBarVie
XposBarViePerdu_P2=(Xpos_P1+LongBarVie)-LongBarViePerdu_P2
pygame.draw.rect(fenetre,VIE,(Xpos_P2,Ypos_P2,LongBarVie,LargBarVie))
pygame.draw.rect(fenetre,MORT,(XposBarViePerdu_P2,Ypos_P2,LongBarViePerdu_P2,LargBarVie))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()