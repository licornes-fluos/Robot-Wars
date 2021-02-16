#!/usr/bin/env python3 
import pygame
import random
import time
from old_sprites import Player
from old_sprites import Direction

def main():
    open = True # Boolean for if window is open or closed
    game_start = False # Boolean for if game has been started
    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    clock.tick(60) # 60 fps limit

    # defining colours for the writing
    ecriture = (236, 121, 250)
    bg = (74, 34, 141)

    #middle of the box where the text  appears
    middle_box = 1360 

    # Initialize Pygame
    pygame.init()

    # defining font
    font = pygame.font.Font('freesansbold.ttf', 67)

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
    #creates the background
    background_image = pygame.image.load("assets/firstpage2.png").convert()
    screen.blit(background_image, [0, 0])

    #creates the text to display for the space pharse
    text_space = font.render('Press Space to start', True, ecriture)
    textRect_space = text_space.get_rect()
    textRect_space.center = (middle_box, 510) # postition
    screen.blit(text_space, textRect_space)

    #create text for ctrl
    text_ctrl = font.render('Press Ctrl to change', True, ecriture)
    textRect_ctrl = text_ctrl.get_rect()
    textRect_ctrl.center = (middle_box, 700) # postition
    screen.blit(text_ctrl, textRect_ctrl)

    #create text for end of text
    text_pl = font.render("the players' keys", True, ecriture)
    textRect_pl = text_pl.get_rect()
    textRect_pl.center = (middle_box, 800) # postition
    screen.blit(text_pl, textRect_pl)

    pygame.display.flip() # updates display window
    
    print("Press SPACE to start.")
    print("Press either CTRL to change keys.")
    
    while open:
    # main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                open = False

            if event.type == pygame.KEYDOWN: # user presses a key
                if not(game_start):

                    if event.key == pygame.K_SPACE: # pressing space starts the game
                        game_start = True


                    # this block can be made into a separate function that takes player key dictionary as argument

                    if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL: # changing key settings on CTRL hit
                        print("changing player 1's keys.")
                        print("press ESC to skip a key.")

                        # erases what was previously written
                        pygame.image.load("assets/bg3.png").convert()
                        screen.blit(background_image, [0, 0])

                        #creates the text to display for the space pharse
                        text_space = font.render('Changing keys for Player 1', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 510) # postition
                        screen.blit(text_space, textRect_space)
                        pygame.display.flip()

                        for i in player1Keys: # browses and prints each element in dictionary
                            next_key = False
                            print(i)

                            while not(next_key): # while loop that stops when user presses desired key
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key != pygame.K_ESCAPE: # if user didn't press ESCAPE, key is changed.
                                            player1Keys[i]=event.key
                                            #print(player1Keys[i])  # for debug; shows number of key added to dictionnary
                                        next_key = True # ends while loop to start algorithm for next move

                        print("changing player 2's keys.")
                        print("press ESC to skip a key.")

                        for i in player2Keys: # same things for player 2
                            next_key = False
                            print(i)

                            while not(next_key):
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key != pygame.K_ESCAPE:
                                            player2Keys[i]=event.key
                                            #print(player2Keys[i])
                                        next_key = True

                        #print(player1Keys,player2Keys)  # also for debug; prints both dictionnaries.

    
                else: #event.type == pygame.KEYDOWN: # user presses a key
                    #if event.key == pygame.K_SPACE: # pressing space starts the game
                    #    start = True
                    if game_start:
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
    
            elif event.type == pygame.KEYUP: # user stops pressing a key
                if game_start:
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
    
    
            # elif event.type == pygame.MOUSEBUTTONDOWN: # user clicks
            #    print("User pressed a mouse button")
    
    
    
        # --- Game logic

        if game_start:     
            pygame.time.delay(30) # updates screen every 30 ms = lowers speed of players (lower = faster, higher = slower)
            player1.move()
            player2.move()

            #loads background image
            background_image = pygame.image.load("assets/bg3.png").convert()
            screen.blit(background_image, [0, 0])
            # draws all the sprites
            all_sprites_list.draw(screen)
            pygame.display.flip()
    
    
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