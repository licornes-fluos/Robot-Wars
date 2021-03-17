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

    def __init__(self, colour, width, height, x, y, screen_width, screen_height, arena_top, arena_bottom, arena_left, arena_right, facing, sprite_image):
        '''
        this is a constructor
        in the parameters, there is the colour, the width and the height
        that are used to define the sprite
        '''
        
        #calls the class (Sprite) constructor, allows the sprite to initialise 
        super().__init__() 
        
        # defines the size of the sprites
        self.width = width
        self.height = height
        
        self.facing = facing
        
        # loads the image
        self.imagebase = sprite_image
        # set the white background of the image to transparent colour
        self.imagebase.set_colorkey()
        self.imagebase = pygame.transform.scale(self.imagebase,(width,height))
        self.image = pygame.transform.rotate(self.imagebase,self.facing)
        
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

    # fetches the rectangle object that has the dimensions (of the image)
    # updates the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.last_shot = pygame.time.get_ticks() # will be used for "def canPlaceBomb"
    
    
    
    def canPlaceBomb(self): # Tests if player can place bomb
        now = pygame.time.get_ticks()
        if now - self.last_shot > 1000 : # the delay is defined here
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
