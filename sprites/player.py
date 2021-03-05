#!/usr/bin/env python3
import pygame
import time

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

    def __init__(self, colour, width, height, x, y, screen_width, screen_height, arena_top, arena_bottom, arena_left, arena_right):
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
        
        # defines the size of the sprites
        self.width = width
        self.height = height

        # defines the height and width of the screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #defines the limits of the arena
        self.arena_top = arena_top
        self.arena_bottom = arena_bottom
        self.arena_left = arena_left
        self.arena_right = arena_right
        # initialises the direction attributes

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
    
        self.last_shot = pygame.time.get_ticks() # will be used for "def canPlaceBomb"
    
    
    def canPlaceBomb(self): # Tests if player can place bomb
        now = pygame.time.get_ticks()
        if now - self.last_shot > 5000 : # the delay is defined here
            self.last_shot = now
            return True
        return False
    
    def hit(self): # Just to check collisions
        print("Player hit")
    
    def start(self):
        self.start = True

# two new classes to separate chunky moving functions from main code ----------------
# DOES NOT WORK; FUNCTIONS ARE CURRENTLY IN MAIN @ LINE 59
"""class Move():
    def __init__(self):
        print("a")
        
    def move1(movingSpeed):
        if player1Up and player1.rect.y >= 0 + 120 :
            player1Facing = "up"
            player1.rect.y -= movingSpeed
        if player1Down and player1.rect.y <= size[1]-20 - 70:
            player1Facing = "down"
            player1.rect.y += movingSpeed
        if player1Left and player1.rect.x >= 0 + 90:
            player1Facing = "left"
            player1.rect.x -= movingSpeed
        if player1Right and player1.rect.x <= size[0]-20 - 90:
            player1Facing = "right"
            player1.rect.x += movingSpeed
        
    def move2(movingSpeed):
        if player2Up and player2.rect.y >= 0 + 120 :
            player2Facing = "up"
            player2.rect.y -= movingSpeed
        if player2Down and player2.rect.y <= size[1]-20 - 70:
            player2Facing = "down"
            player2.rect.y += movingSpeed
        if player2Left and player2.rect.x >= 0 + 90:
            player2Facing = "left"
            player2.rect.x -= movingSpeed
        if player2Right and player2.rect.x <= size[0]-20 - 90:
            player2Facing = "right"
            player2.rect.x += movingSpeed
# ------------------------------------------------------------------------------------"""
