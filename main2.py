# j'ai fusionné main1 avec le script amélioré de Rachel pour les sprites. À ensuite voir comment séparer les 2 at appeler l'algo sprites depuis main mais ça marche.

import pygame
import random
import time

pygame.init() #initialises the window

size = (800, 600) # width,height
screen = pygame.display.set_mode(size) #sets size of popup window

pygame.display.set_caption("Robot Wars") # sets title of game window

# Defining some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
PURPLE   = (150, 0, 255)

open = True # Boolean for if window is open or closed
clock = pygame.time.Clock() # Used to manage how fast the screen updates
clock.tick(60) # 60 fps limit

class Player(pygame.sprite.Sprite):
    '''
    this class defines the first player
    it uses 'Sprite' class in Pygame
    '''
    def __init__(self, colour, width, height):
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

# creates a list of every sprite, only contains the player for now, but will eventually contain the bombs as well
all_sprites_list = pygame.sprite.Group()

# creates a first player which is purple and adds it to
player1 = Player(PURPLE, 20, 20)
all_sprites_list.add(player1)

screen.fill(WHITE) # fills window with white
pygame.display.flip() # updates display window

while open:
    # main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            open = False
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    # --- Game logic




    # --- Drawing code

    # gets the mouse position
    # returns it as a list of two numbers
    pos = pygame.mouse.get_pos()

    # fetches the x and y out of the list
    # sets the player object to the mouse location
    player1.rect.x = pos[0]
    player1.rect.y = pos[1]

    # checks if the player block has collided with anything,
    #will be used later for the bombs
    #to be modified according to the game,
    #maybe do not use boolean as it takes the sprite out of block_list
    blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, True)
    # draws all the spites
    screen.fill(WHITE) # fills window with white
    all_sprites_list.draw(screen)
    pygame.display.flip()

# quits window once while loop is closed (open = False)
pygame.quit()
