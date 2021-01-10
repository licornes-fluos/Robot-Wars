#!/usr/bin/env python3
import pygame

# creates colours that will be used for the sprites
PURPLE= (150, 0, 255)
GREEN= (0, 255, 0)
WHITE= (255, 255, 255)

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
        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# creates a list of 'sprites.' every block in the program is added to this list
# for now there is nothing in it, as sprites are not part of this list
# it will include the blocks for example the bombs
# it uses a class called Group
block_list = pygame.sprite.Group()
 
# creates a list of every sprite, only contains the player for now, but will eventually contain the bombs as well
all_sprites_list = pygame.sprite.Group()

# creates a first player which is purple and adds it to 
player1 = Player(PURPLE, 20, 20)
all_sprites_list.add(player1)

# loops until the user clicks the close button.
done = False
 
# used to manage how fast the screen updates, uses class Clock from Pygame
clock = pygame.time.Clock()

#/!/ change and link to Aline's part for actual background

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
    
    # end of link

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
    all_sprites_list.draw(screen)

    # /!/ link to Aline's prgram
    # Limit to 60 frames per second
    clock.tick(60)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
# end link