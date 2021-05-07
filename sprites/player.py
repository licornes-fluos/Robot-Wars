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

    def __init__(self, colour, width, height, x, y, screen_width, screen_height, arena_top, arena_bottom, arena_left, arena_right, facing, sprite_image, speed, hp):
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
        
        self.speed = speed
        
        # not moving or attacking yet
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.attack = False
        self.speed_boost = False
        
        # loads the image
        self.imagebase = sprite_image
        
        # set the white background of the image to transparent colour
        self.imagebase.set_colorkey()
        # base image set to width and height defined above
        self.imagebase = pygame.transform.scale(self.imagebase,(width,height))
        # image rotated depending on where robot is facing
        self.image = pygame.transform.rotate(self.imagebase,self.facing)
        
        # defines the height and width of the screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #defines the limits of the arena
        self.arena_top = arena_top
        self.arena_bottom = arena_bottom
        self.arena_left = arena_left
        self.arena_right = arena_right
        
        self.hp = hp

        self.start = False

        self.explosions_collided = pygame.sprite.Group()

    # fetches the rectangle object that has the dimensions (of the image)
    # updates the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.last_shot = pygame.time.get_ticks() # will be used for "def canPlaceBomb"
        
    def move(self):
        if self.up and self.rect.y >= self.arena_top :
            self.facing = 180
            self.rect.y -= self.speed
        if self.down and self.rect.y <= self.arena_bottom:
            self.facing = 0
            self.rect.y += self.speed
        if self.left and self.rect.x >= self.arena_left:
            self.facing = -90
            self.rect.x -= self.speed
        if self.right and self.rect.x <= self.arena_right:
            self.facing = 90
            self.rect.x += self.speed
    
    def updateSpriteImage(self):
        self.image = pygame.transform.rotate(self.imagebase,self.facing)
    
    def canPlaceBomb(self): # Tests if player can place bomb
        now = pygame.time.get_ticks()
        if now - self.last_shot > 1000 : # the delay is defined here
            self.last_shot = now
            return True
        return False
    
    def start(self):
        self.start = True

    def addExplosionHits(self, explosions):
        '''
        Add explosions to the list of those that have collided with the player
        '''
        self.explosions_collided.add(explosions)

    def differenceExplosions(self, explosions):
        '''
        Calculates the difference between the set of explosions that have already
        collided with the player, and the full list of ongoing explosions.
        '''
        explosions_copy = explosions.copy()
        explosions_copy.remove(self.explosions_collided)
        return explosions_copy
