#!/usr/bin/env python3 
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480))

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
  continue #Je place continue ici pour pouvoir relancer la boucle infinie
                 #mais il est d'habitude remplacé par une suite d'instructions
import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
  continuer = int(input())  
