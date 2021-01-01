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
start = False # Boolean for if game has been started
clock = pygame.time.Clock() # Used to manage how fast the screen updates
clock.tick(60) # 60 fps limit

        # ---------------------------- will need to be put in separate "player" module and imported here
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
        # -------------------------

player1Up = bool()    # boolean values will be true if player is going in associated direction, false if not.
player1Down = bool()
player1Left = bool()
player1Right = bool()

player2Up = bool()
player2Down = bool()
player2Left = bool()
player2Right = bool()

player1Keys = {"up":pygame.K_i,"down":pygame.K_k,"left":pygame.K_j,"right":pygame.K_l,"attack":pygame.K_n}
player2Keys = {"up":pygame.K_w,"down":pygame.K_s,"left":pygame.K_a,"right":pygame.K_d,"attack":pygame.K_c}

player1Facing = str() # string variables for direction players are facing, will be used to direct attacks.
player2Facing = str()

# creates a list of every sprite, only contains the player for now, but will eventually contain the bombs as well
all_sprites_list = pygame.sprite.Group()

# creates a first player which is purple and adds it to the list
player1 = Player(RED, 30, 30)
player2 = Player(BLUE, 30, 30)
all_sprites_list.add(player1,player2)

player1.rect.x = 550 #sets player 1 base position to x=550 y=290
player1.rect.y = 290
player2.rect.x = 230 #sets player 2 base position to x=230 y=290
player2.rect.y = 290

screen.fill(WHITE) # fills window with white
pygame.display.flip() # updates display window

print("Press SPACE to start.")
print("Press either CTRL to change keys.")

while open:
    # main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            open = False
            print("Quit")

        if event.type == pygame.KEYDOWN: # user presses a key
            if event.key == pygame.K_SPACE: # pressing space starts the game
                start = True
            if start:
                if event.key == player1Keys["up"]:
                    player1Up = True
                if event.key == player2Keys["up"]:
                    player2Up = True

                if event.key == player1Keys["down"]:
                    player1Down = True
                if event.key == player2Keys["down"]:
                    player2Down = True

                if event.key == player1Keys["left"]:
                    player1Left = True
                if event.key == player2Keys["left"]:
                    player2Left = True

                if event.key == player1Keys["right"]:
                    player1Right = True
                if event.key == player2Keys["right"]:
                    player2Right = True

        elif event.type == pygame.KEYUP: # user stops pressing a key
            if start:
                if event.key == player1Keys["up"]:
                    player1Up = False
                if event.key == player2Keys["up"]:
                    player2Up = False

                if event.key == player1Keys["down"]:
                    player1Down = False
                if event.key == player2Keys["down"]:
                    player2Down = False

                if event.key == player1Keys["left"]:
                    player1Left = False
                if event.key == player2Keys["left"]:
                    player2Left = False

                if event.key == player1Keys["right"]:
                    player1Right = False
                if event.key == player2Keys["right"]:
                    player2Right = False


        # elif event.type == pygame.MOUSEBUTTONDOWN: # user clicks
        #    print("User pressed a mouse button")


    # --- Game logic
    pygame.time.delay(30)
    if player1Up and player1.rect.y >= 0 + 120 :
        player1Facing = "up"
        player1.rect.y -= 10
        pygame.display.flip()
    if player1Down and player1.rect.y <= size[1]-20 - 70:
        player1Facing = "down"
        player1.rect.y += 10
        pygame.display.flip()
    if player1Left and player1.rect.x >= 0 + 90:
        player1Facing = "left"
        player1.rect.x -= 10
        pygame.display.flip()
    if player1Right and player1.rect.x <= size[0]-20 - 90:
        player1Facing = "right"
        player1.rect.x += 10
        pygame.display.flip()

    if player2Up and player2.rect.y >= 0 + 120 :
        player2Facing = "up"
        player2.rect.y -= 10
        pygame.display.flip()
    if player2Down and player2.rect.y <= size[1]-20 - 70:
        player2Facing = "down"
        player2.rect.y += 10
        pygame.display.flip()
    if player2Left and player2.rect.x >= 0 + 90:
        player2Facing = "left"
        player2.rect.x -= 10
        pygame.display.flip()
    if player2Right and player2.rect.x <= size[0]-20 - 90:
        player2Facing = "right"
        player2.rect.x += 10
        pygame.display.flip()


    # --- Drawing code

    # gets the mouse position
    # returns it as a list of two numbers
    #pos = pygame.mouse.get_pos()

    # fetches the x and y out of the list
    # sets the player object to the mouse location
    #player1.rect.x = pos[0]-10
    #player1.rect.y = pos[1]-9
    if start:
    #loads background image
        background_image = pygame.image.load("C:/Users/Aline/Documents/0 Docs/Devoirs/1ere/robotwars/assets/bg.png").convert()
        screen.blit(background_image, [0, 0])
    # draws all the spites
        all_sprites_list.draw(screen)
        pygame.display.flip()

# quits window once while loop is closed (open = False)
pygame.quit()