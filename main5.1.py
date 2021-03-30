#!/usr/bin/env python3 
import pygame
import time
from sprites import Player
from bombs import Bombs
from HP import Barre_vie
#from bombs import class_Bombs
#from sprites import Move

def main():   
    # Initialize Pygame
    pygame.init()
    
    open = True # Boolean for if window is open or closed
    game_start = False # Boolean for if game has been started

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    clock.tick(30) # 30 fps cap
    
    # sets size of the screen
    size = (int(pygame.display.Info().current_w),int((pygame.display.Info().current_w*9)/16)) # width,height
    
    screen = pygame.display.set_mode(size) #sets size of popup window
    
    #function to cleanly change "magic numbers" to fit all resolutions
    def resized(x):
        return size[0]/(1920/x)
    
    # defining colours for the writing
    ecriture = (236, 121, 250)
    bg = (74, 34, 141)

    # defining font
    font = pygame.font.Font('freesansbold.ttf', int(resized(67)))
    
    #size of the arena. up down left right
    limit_arena = (resized(241), size[1]-resized(240), resized(117), size[0]-resized(235))
    
    #sets size of player 1 and 2
    size1 = int(resized(120)), int(resized(120))
    size2 = int(resized(120)), int(resized(120))


    #middle of the box where the text  appears
    middle_box = resized(1360)
    
    # creates a list of 'sprites.' that will contain BOMBS ONLY
    block_list = pygame.sprite.Group()
    # creates a list of 'sprites.' that will contain EXPLOSIONS ONLY
    explosion_list = pygame.sprite.Group()
    # creates a list of every sprite (explosions and bombs included)
    all_sprites_list = pygame.sprite.Group()
    
    player1Keys = {"up":pygame.K_e,"down":pygame.K_d,"left":pygame.K_s,"right":pygame.K_f,"attack":pygame.K_v}
    player2Keys = {"up":pygame.K_i,"down":pygame.K_k,"left":pygame.K_j,"right":pygame.K_l,"attack":pygame.K_n}
    
    # health of player
    pv_player1 = 100
    pv_player2 = 100

    # create health bar. (self, pv, pvmax, xpos, ypos, longu, larg, c_vie, c_mort)
    life_bar1 = Barre_vie(pv_player1, 100, resized(330), resized(110), resized(495), resized(75), (35, 145, 140), (4, 96, 104))
    life_bar2 = Barre_vie(pv_player2, 100, resized(1105), resized(110), resized(495), resized(75), (186, 106, 202), (87, 42, 125))

    # string variables for direction players are facing, will be used to direct attacks.
    player1Facing = 90
    player2Facing = -90
    
    player1Speed = 10
    player2Speed = 10
    
    player1ImageBase = pygame.image.load("assets/spider sprite og resolution.png").convert_alpha()
    player2ImageBase = pygame.image.load("assets/tank sprite og resolution.png").convert_alpha()
    
    # creates a first player which is purple and adds it to 
    player1 = Player(Player.PURPLE, size1[0], size1[1], size[0]//3, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3], player1Facing, player1ImageBase, player1Speed)
    all_sprites_list.add(player1)
    
    # creates second player
    player2 = Player(Player.GREEN, size2[0], size2[1], size[0]//3*2, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3], player2Facing, player2ImageBase, player2Speed)
    all_sprites_list.add(player2)
    
    #function to create text to display for the space pharse
    def write(text,coord):
        text_space = font.render(text, True, ecriture)
        textRect_space = text_space.get_rect()
        textRect_space.center = (middle_box, coord) # postition
        screen.blit(text_space, textRect_space)
        
    #screen.fill(Player.WHITE) # fills window with white
    background_image = pygame.image.load("assets/firstpage3.png").convert()
    background_image = pygame.transform.scale(background_image, size)
    screen.blit(background_image, [0, 0])
    
    #creates the text to display for the space pharse
    write('Press SPACE to start',resized(510))

    #create text for ctrl
    write('Press CTRL to change',resized(700))

    #create text for end of text
    write("the players' keys",resized(800))

    pygame.mixer.music.load("assets/Simon_Bichbihler_In_the_1980s.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    pygame.display.flip() # updates display window 
    
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

                        # erases what was previously written
                        pygame.image.load("assets/bg3.png").convert()
                        screen.blit(background_image, [0, 0])

                        #creates the text to display for the space pharse
                        write('Changing keys for Player 1',resized(420))
                        write('Change in order:',resized(550))
                        write('UP, DOWN, LEFT,',resized(630))
                        write('RIGHT, ATTACK',resized(710))
                        write('ESCAPE to skip a key',resized(820))

                        pygame.display.flip()

                        for i in player1Keys: # browses and prints each element in dictionary
                            next_key = False
                            #pygame.image.load("assets/bg3.png").convert()
                            #screen.blit(background_image, [0, 0])
                            #write(str(i),630)
                            while not(next_key): # while loop that stops when user presses desired key
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key != pygame.K_ESCAPE: # if user didn't press ESCAPE, key is changed.
                                            player1Keys[i]=event.key
                                            #print(player1Keys[i])  # for debug; shows number of key added to dictionnary
                                        next_key = True # ends while loop to start algorithm for next move


                        # erases what was previously written
                        pygame.image.load("assets/bg3.png").convert()
                        screen.blit(background_image, [0, 0])

                        #creates the text to display for the space pharse
                        write('Changing keys for Player 2',resized(420))
                        write('Change in order:',resized(550))
                        write('UP, DOWN, LEFT,',resized(630))
                        write('RIGHT, ATTACK',resized(710))
                        write('ESCAPE to skip a key',resized(820))
                        write('SPACE to play',resized(920))

                        pygame.display.flip()

                        for i in player2Keys: # same things for player 2
                            next_key = False
                            
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
                        player1.up = True
                    if event.key == player2Keys["up"]:
                        player2.up = True
    
                    if event.key == player1Keys["down"]:
                        player1.down = True
                    if event.key == player2Keys["down"]:
                        player2.down = True
    
                    if event.key == player1Keys["left"]:
                        player1.left = True
                    if event.key == player2Keys["left"]:
                        player2.left = True
    
                    if event.key == player1Keys["right"]:
                        player1.right = True
                    if event.key == player2Keys["right"]:
                        player2.right = True
    
                    if event.key == player1Keys["attack"]:
                        player1.attack = True
                    if event.key == player2Keys["attack"]:
                        player2.attack = True
    
            elif event.type == pygame.KEYUP: # user stops pressing a key
                if game_start:
                    if event.key == player1Keys["up"]:
                        player1.up = False
                    if event.key == player2Keys["up"]:
                        player2.up = False
    
                    if event.key == player1Keys["down"]:
                        player1.down = False
                    if event.key == player2Keys["down"]:
                        player2.down = False
    
                    if event.key == player1Keys["left"]:
                        player1.left = False
                    if event.key == player2Keys["left"]:
                        player2.left = False
    
                    if event.key == player1Keys["right"]:
                        player1.right = False
                    if event.key == player2Keys["right"]:
                        player2.right = False
    
                    if event.key == player1Keys["attack"]:
                        player1.attack = False
                    if event.key == player2Keys["attack"]:
                        player2.attack = False
    
    
        # --- Game logic

        if game_start:
            
            # defines how many milliseconds until next frame update
            pygame.time.delay(5)
            
            # calls tests from functions up top
            player1.move()
            player2.move()
            
            #loads background image
            background_image = pygame.image.load("assets/bg3.png").convert()
            background_image = pygame.transform.scale(background_image, size)
            screen.blit(background_image, [0, 0])
            
            player1.updateSpriteImage()
            player2.updateSpriteImage()
            
            # draws all the sprites
            all_sprites_list.draw(screen)

        

            Bombs.manageBomb(player1, block_list, player1.attack,  all_sprites_list, explosion_list, resized(250)) # Calling the function manageBomb in the file Bombs.py
            Bombs.manageBomb(player2, block_list, player2.attack,  all_sprites_list, explosion_list, resized(250)) # Calling the function manageBomb in the file Bombs.py
            life_bar1.barres(screen)
            life_bar2.barres(screen)
            
            pygame.display.flip()
    # quits window once while loop is closed (open = False)
    pygame.quit()

if __name__ == '__main__': #avoid running main code when loaded as a module
    main()
