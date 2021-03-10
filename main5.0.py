#!/usr/bin/env python3 
import pygame
import time
from sprites import Player
from bombs import Bombs
from HP import Barre_vie
#from bombs import class_Bombs
#from sprites import Move

def main():
    open = True # Boolean for if window is open or closed
    game_start = False # Boolean for if game has been started
    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    clock.tick(30) # 30 fps cap
    
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
    sprite = (40, 40)
    screen = pygame.display.set_mode(size) #sets size of popup window

    # creates a list of 'sprites.' that will contain sprites other than the players
    block_list = pygame.sprite.Group()
    
    # creates a list of every sprite, only contains the player for now, but will eventually contain the bombs as well
    all_sprites_list = pygame.sprite.Group()
    
    player1Keys = {"up":pygame.K_e,"down":pygame.K_d,"left":pygame.K_s,"right":pygame.K_f,"attack":pygame.K_v}
    player2Keys = {"up":pygame.K_i,"down":pygame.K_k,"left":pygame.K_j,"right":pygame.K_k,"attack":pygame.K_n}
    
    # creates a first player which is purple and adds it to 
    player1 = Player(Player.PURPLE, sprite[0], sprite[1], size[0]//3, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3])
    all_sprites_list.add(player1)
    
    # creates second player
    player2 = Player(Player.GREEN, sprite[0], sprite[1], size[0]//3*2, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3])
    all_sprites_list.add(player2)
    
    # create health bar
    life_bar1 = Barre_vie(80, 100, 330, 110, 495, 75)
    life_bar2 = Barre_vie(70, 100, 1105, 110, 495, 75)

    # boolean values will be true if player is going in associated direction, false if not.
    player1Up = bool()
    player1Down = bool()
    player1Left = bool()
    player1Right = bool()
    player1Attack = bool()
    
    player2Up = bool()
    player2Down = bool()
    player2Left = bool()
    player2Right = bool()
    player2Attack = bool()
    
    # string variables for direction players are facing, will be used to direct attacks.
    player1Facing = str()
    player2Facing = str()
    
    player1Speed = 10
    player2Speed = 10
    
    def move1(movingSpeed):
        if player1Up and player1.rect.y >= limit_arena[0] :
            player1Facing = "up"
            player1.rect.y -= movingSpeed
        if player1Down and player1.rect.y <= size[1] - limit_arena[1] - sprite[0]:
            player1Facing = "down"
            player1.rect.y += movingSpeed
        if player1Left and player1.rect.x >= 0 + limit_arena[2]:
            player1Facing = "left"
            player1.rect.x -= movingSpeed
        if player1Right and player1.rect.x <= size[0] - limit_arena[3] - sprite[1]:
            player1Facing = "right"
            player1.rect.x += movingSpeed
        
    def move2(movingSpeed):
        if player2Up and player2.rect.y >= limit_arena[0] :
            player2Facing = "up"
            player2.rect.y -= movingSpeed
        if player2Down and player2.rect.y <= size[1]- limit_arena[1] - sprite[0]:
            player2Facing = "down"
            player2.rect.y += movingSpeed
        if player2Left and player2.rect.x >= 0 + limit_arena[2]:
            player2Facing = "left"
            player2.rect.x -= movingSpeed
        if player2Right and player2.rect.x <= size[0]- limit_arena[3] - sprite[1]:
            player2Facing = "right"
            player2.rect.x += movingSpeed
    
    #screen.fill(Player.WHITE) # fills window with white
    background_image = pygame.image.load("assets/firstpage2.png").convert()
    background_image = pygame.transform.scale(background_image, size)
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
                        textRect_space.center = (middle_box, 420) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('Press desired keys', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 550) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('in the following order:', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 630) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('UP, DOWN, LEFT,', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 710) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('RIGHT, ATTACK', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 790) # postition
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

                        # erases what was previously written
                        pygame.image.load("assets/bg3.png").convert()
                        screen.blit(background_image, [0, 0])

                        #creates the text to display for the space pharse
                        text_space = font.render('Changing keys for Player 2', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 420) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('Press desired keys', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 550) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('in the following order:', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 630) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('UP, DOWN, LEFT,', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 710) # postition
                        screen.blit(text_space, textRect_space)

                        text_space = font.render('RIGHT, ATTACK', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 790) # postition
                        screen.blit(text_space, textRect_space)
                        
                        text_space = font.render('Space to play', True, ecriture)
                        textRect_space = text_space.get_rect()
                        textRect_space.center = (middle_box, 920) # postition
                        screen.blit(text_space, textRect_space)

                        pygame.display.flip()

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

    
                else:
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
    
                    if event.key == player1Keys["attack"]:
                        player1Attack = True
                    if event.key == player2Keys["attack"]:
                        player2Attack = True
    
            elif event.type == pygame.KEYUP: # user stops pressing a key
                if game_start:
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
    
                    if event.key == player1Keys["attack"]:
                        player1Attack = False
                    if event.key == player2Keys["attack"]:
                        player2Attack = False
    
    
            # elif event.type == pygame.MOUSEBUTTONDOWN: # user clicks
    
    
    
        # --- Game logic

        if game_start:
            # defines how many milliseconds until next frame update
            pygame.time.delay(5)
            
            # calls tests from functions up top
            move1(player1Speed)
            move2(player2Speed)
            
            # if player1Attack :
            #     bomb1.rect.x = player1.rect.x + 5 # le "+5" c'est juste pour centrer la bombe
            #     bomb1.rect.y = player1.rect.y + 5
            # if player2Attack :
            #     bomb2.rect.x = player2.rect.x + 5
            #     bomb2.rect.y = player2.rect.y + 5
            

            #loads background image
            background_image = pygame.image.load("assets/bg3.png").convert()
            background_image = pygame.transform.scale(background_image, size)
            screen.blit(background_image, [0, 0])
            # draws all the sprites
            all_sprites_list.draw(screen)
        
            Bombs.manageBomb(player1, block_list, player1Attack,  all_sprites_list) # Calling the function manageBomb in the file Bombs.py
            Bombs.manageBomb(player2, block_list, player2Attack,  all_sprites_list) # Calling the function manageBomb in the file Bombs.py
            life_bar1.barres(screen)
            life_bar2.barres(screen)
            pygame.display.flip()

        
        # checks if the player block has collided with anything, 
        #will be used later for the bombs
        #to be modified according to the game, 
        #maybe do not use boolean as it takes the sprite out of block_list
        # blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, True)
        # blocks_hit_list = pygame.sprite.spritecollide(player2, block_list, True)
    
    
    # quits window once while loop is closed (open = False)
    pygame.quit()

if __name__ == '__main__': #avoid running main code when loaded as a module
    main()