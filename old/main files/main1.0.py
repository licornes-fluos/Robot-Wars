import pygame
import random
import time

pygame.init() #initialises the window

size = (800, 600)
screen = pygame.display.set_mode(size) #sets size of popup window

pygame.display.set_caption("Robot Wars") # sets title of game window

# Defining some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

open = True # Boolean for if window is open or closed
clock = pygame.time.Clock() # Used to manage how fast the screen updates

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
            
    screen.fill(WHITE) # fills window with white
    pygame.display.flip() # updates display window
    clock.tick(60) # 60 fps limit
    
    background_image = pygame.image.load("U:/Documents/Devoirs/Robot Wars/assets/background.jpg").convert()
    #add more code to show bg https://self-learning-java-tutorial.blogspot.com/2015/12/pygame-setting-background-image.html
    pygame.display.flip()

# quits window once while loop is closed (open = False)
pygame.quit()
