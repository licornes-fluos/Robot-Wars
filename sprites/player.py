#!/usr/bin/env python3
import pygame
import random
import time
from enum import Enum

class Direction(Enum):
    Stopped = 0
    Up = 1
    Down = 2
    Left = 3
    Right = 4

class Player(pygame.sprite.Sprite):
    '''
    this class defines the first player
    it uses 'Sprite' class in Pygame
    '''

    # CLASS ATTRIBUTES : creates colours that will be used for the sprites
    PURPLE   = (150, 0, 255)
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 220,   150)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)

    def __init__(self, colour, width, height, x, y, screen_width, screen_height):
        '''
        this is a constructor
        in the parameters, there is the colour, the width and the height
        that are used to define the sprite
        '''
        
        #calls the class (Sprite) constructor, allows the sprite to initialise 
        super().__init__() 
        
        # creates an image of the block
        # fills it with a colour.
        self.image = pygame.Surface([width, height])
        self.image.fill(colour) 
        
        self.width = width
        self.height = height

        self.screen_width = screen_width
        self.screen_height = screen_height
        # initialises the direction attributes
        self.direction = Direction.Stopped

        self.start = False

    # to use an image instead of a colour:
    #def __init__(self):
    
        # calls the class (Sprite) constructor, allows the sprite to initialise 
        #super().__init__()
        
        # loads the image
        #self.image = pygame.image.load("player.png").convert()
        
        # set the white background of the image to transparent colour
        #self.image.set_colorkey(WHITE)
        
    # fetches the rectangle object that has the dimensions (of the image)
    # updates the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def start_moving(self, direction):
        self.direction = direction
    
    def stop_moving(self):
        self.direction = Direction.Stopped

    def move(self):
        if self.direction == Direction.Stopped:
            return
        elif self.direction == Direction.Up and self.rect.y >= 0 + 120 :
            self.rect.y -= 10
        elif self.direction == Direction.Down and self.rect.y <= self.screen_height - self.height - 70:
            self.rect.y += 10
        elif self.direction == Direction.Left and self.rect.x >= 0 + 90:
            self.rect.x -= 10
        elif self.direction == Direction.Right and self.rect.x <= self.screen_width - self.width - 90:
            self.rect.x += 10
    
    def start(self):
        self.start = True
