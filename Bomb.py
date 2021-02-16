#!/usr/bin/env python3
import pygame
import random
import time
from sprites import Player
from sprites import Direction


# --------------------------------------------------------------
class Bombs(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):

        #calls the class (Bombs) constructor, allows the sprite to initialise
        super().__init__()

        # creates an image of the block
        # fills it with a colour.
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
    # updates the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


# for an image
    # def __init__(self,x,y):
        # pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load('Enemy.gif').convert()
        # self.rect = self.image.get_rect(x=x, y=y)


    # def delay:
        # running = 1
        # counter = 0
        # while running:
            # pygame.time.delay(10)

    # counter += 1
        # if counter >= 200:
            # enemyship_sprites.add(Enemy(320))
        # counter = 0

    # def exploded(self):
        # for enemy in all_sprites_list:
            # if enemy.rect.x<100:
                 # all_sprites_list(enemy)


    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
    # colliderect() is a test to see if two rectangles overlap. It returns true if any portion of either rectangle overlap (except the top+bottom or left+right edges)).
# --------------------------------------------------------------



def main():
    open = True # Boolean for if window is open or closed
    start = False # Boolean for if game has been started
    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    clock.tick(60) # 60 fps limit


    # Initialize Pygame
    pygame.init()

    # sets size of the screen
    size = (1920, 1080) # width,height
    limit_arena = (241, 115, 115, 115) #size of the arena
    screen = pygame.display.set_mode(size) #sets size of popup window

    # creates a list of 'sprites.' that will contain sprites other than the players
    block_list = pygame.sprite.Group()

    # creates a list of every sprite, only contains the player for now, but will eventually contain the bombs as well
    all_sprites_list = pygame.sprite.Group()


    player1Keys = {"up":pygame.K_i,"down":pygame.K_k,"left":pygame.K_j,"right":pygame.K_l,"attack":pygame.K_n}
    player2Keys = {"up":pygame.K_e,"down":pygame.K_d,"left":pygame.K_s,"right":pygame.K_f,"attack":pygame.K_v}

    # creates a first player which is purple and adds it to
    player1 = Player(Player.PURPLE, 40, 40, size[0]//3*2, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3])
    all_sprites_list.add(player1)

    # creates second player
    player2 = Player(Player.GREEN, 40, 40, size[0]//3, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3])
    all_sprites_list.add(player2)


    #screen.fill(Player.WHITE) # fills window with white
    background_image = pygame.image.load("assets/firstpage1.png").convert()
    screen.blit(background_image, [0, 0])
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
                        player1.start_moving(Direction.Up)
                    if event.key == player2Keys["up"]:
                        player2.start_moving(Direction.Up)

                    if event.key == player1Keys["down"]:
                        player1.start_moving(Direction.Down)
                    if event.key == player2Keys["down"]:
                        player2.start_moving(Direction.Down)

                    if event.key == player1Keys["left"]:
                        player1.start_moving(Direction.Left)
                    if event.key == player2Keys["left"]:
                        player2.start_moving(Direction.Left)

                    if event.key == player1Keys["right"]:
                        player1.start_moving(Direction.Right)
                    if event.key == player2Keys["right"]:
                        player2.start_moving(Direction.Right)

# -------------------------------------------------------------------
                    if event.key == player1Keys["attack"]:
                        player1Attack = True
                    if event.key == player2Keys["attack"]:
                        player2Attack = True
# --------------------------------------------------------------------


            elif event.type == pygame.KEYUP: # user stops pressing a key
                if start:
                    if event.key == player1Keys["up"]:
                        player1.stop_moving()
                    if event.key == player2Keys["up"]:
                        player2.stop_moving()

                    if event.key == player1Keys["down"]:
                        player1.stop_moving()
                    if event.key == player2Keys["down"]:
                        player2.stop_moving()

                    if event.key == player1Keys["left"]:
                        player1.stop_moving()
                    if event.key == player2Keys["left"]:
                        player2.stop_moving()

                    if event.key == player1Keys["right"]:
                        player1.stop_moving()
                    if event.key == player2Keys["right"]:
                        player2.stop_moving()

# -----------------------------------------------------------------------
                    if event.key == player1Keys["attack"]:
                        player1Attack = False
                    if event.key == player2Keys["attack"]:
                        player2Attack = False
# -------------------------------------------------------------------------



            # elif event.type == pygame.MOUSEBUTTONDOWN: # user clicks
            #    print("User pressed a mouse button")



        # --- Game logic

        if start:
            pygame.time.delay(30) # updates screen every 30 ms = lowers speed of players (lower = faster, higher = slower)
            player1.move()
            player2.move()

            #loads background image
            background_image = pygame.image.load("assets/bg2.png").convert()
            screen.blit(background_image, [0, 0])
            # draws all the sprites
            all_sprites_list.draw(screen)
            pygame.display.flip()


# --------------------------------------------------------------------------
            if player1Attack :
                get_rawtime() # in milliseconds
                bomb1 = Bombs(BLACK, 20, 20) # creates the bomb for the player
                bomb1.rect.x = player1.rect.x + 5 # Affiche la bombe aux coordonnées du joueur
                bomb1.rect.y = player1.rect.y + 5 # le "+5" c'est juste pour centrer la bombe
                block_list.add(bomb1)
                if bomb1.is_collided_with(player2):
                    print('collision!')
                    # player2.kill()

            if player2Attack :
                bomb2 = Bombs(BLACK, 20, 20)
                bomb2.rect.x = player2.rect.x + 5
                bomb2.rect.y = player2.rect.y + 5
                block_list.add(bomb2)
                if bomb2.is_collided_with(player1):
                    print('collision!')
                    # player1.kill()
# -------------------------------------------------------------------------


    #/!/ change and link to Aline's part for actual background

    # loops until the user clicks the close button.
    #done = False

    # used to manage how fast the screen updates, uses class Clock from Pygame
    #clock = pygame.time.Clock()

    # Set the height and width of the screen
    #screen_width = 800
    #screen_height = 600
    #screen = pygame.display.set_mode([screen_width, screen_height])



    #while not done:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            done = True

        # Clear the screen
    #    screen.fill(WHITE)

        # end of link

        # gets the mouse position
        # returns it as a list of two numbers
    #    pos = pygame.mouse.get_pos()

        # fetches the x and y out of the list
        # sets the player object to the mouse location
        #player1.rect.x = pos[0]
        #player1.rect.y = pos[1]

        # temporary position for the second player
        #player2.rect.x = 220
        #player2.rect.y = 100

        # checks if the player block has collided with anything,
        #will be used later for the bombs
        #to be modified according to the game,
        #maybe do not use boolean as it takes the sprite out of block_list
        blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, True)
        blocks_hit_list = pygame.sprite.spritecollide(player2, block_list, True)


        # /!/ link to Aline's prgram

           # draws all the spites
        #all_sprites_list.draw(screen)


    # quits window once while loop is closed (open = False)
    pygame.quit()

        # Go ahead and update the screen with what we've drawn.
        #pygame.display.flip()
        #pygame.display.update()

    #pygame.quit()
    # end link

if __name__ == '__main__': #avoid running main code when loaded as a module
    main()