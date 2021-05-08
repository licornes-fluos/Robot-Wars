#!/usr/bin/env python3 
import pygame
import time
from sprites import Player
from bombs import Bombs
from HP import Barre_vie

# setting default keys to play
player1Keys = {"up":pygame.K_e,"down":pygame.K_d,"left":pygame.K_s,"right":pygame.K_f,"attack":pygame.K_v}
player2Keys = {"up":pygame.K_i,"down":pygame.K_k,"left":pygame.K_j,"right":pygame.K_l,"attack":pygame.K_n}

def main():   
    # global variables aren't reinitialized if main is called again
    global player1Keys
    global player2Keys
    
    # health of players
    hp_player1 = 100
    hp_player2 = 100
    
    # speed of players (number of pixels that they can move every tick)
    player1Speed = 3
    player2Speed = 3
    
    # string variables for direction players are facing, will be used to direct attacks.
    player1Facing = 90
    player2Facing = -90
    
    # Initialize Pygame
    pygame.init()
    
    # sets size of the screen
    size = (int(pygame.display.Info().current_w),int((pygame.display.Info().current_w*9)/16))
    screen = pygame.display.set_mode(size)
     
    #function to cleanly change "magic numbers" to fit all resolutions
    def resized(x):
        return size[0]/(1920/x)
    
    #function to create text to display for the space pharse
    def write(text,xcoord,ycoord):
        font = pygame.font.Font('freesansbold.ttf', int(resized(67)))
        text_space = font.render(text, True, (236, 121, 250))
        textRect_space = text_space.get_rect()
        textRect_space.center = (resized(ycoord), resized(xcoord)) # postition
        screen.blit(text_space, textRect_space)
        
    #size of the arena. up down left right
    limit_arena = (resized(241), size[1]-resized(240), resized(117), size[0]-resized(235))
    
    clock = pygame.time.Clock() # Used to manage how often the screen updates
    clock.tick(30) # 30 fps cap
    
    #sets size of player 1 and 2
    size1 = int(resized(120)), int(resized(120))
    size2 = int(resized(120)), int(resized(120))
    
    # base images of player sprites, are altered in Player class using facing variable
    player1ImageBase = pygame.image.load("assets/spider sprite og resolution.png").convert_alpha()
    player2ImageBase = pygame.image.load("assets/tank sprite og resolution.png").convert_alpha()
    
    # creates players
    player1 = Player(Player.PURPLE, size1[0], size1[1], size[0]//3, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3], player1Facing, player1ImageBase, player1Speed, hp_player1)
    player2 = Player(Player.GREEN, size2[0], size2[1], size[0]//3*2, size[1]//2, size[0], size[1], limit_arena[0], limit_arena[1], limit_arena[2], limit_arena[3], player2Facing, player2ImageBase, player2Speed, hp_player2)
    
    # create health bar. (self, hp, hpmax, xpos, ypos, longu, larg, c_vie, c_mort)
    life_bar1 = Barre_vie(player1.hp, hp_player1, resized(330), resized(110), resized(495), resized(75), (35, 145, 140), (4, 96, 104))
    life_bar2 = Barre_vie(player2.hp, hp_player2, resized(1105), resized(110), resized(495), resized(75), (186, 106, 202), (87, 42, 125))
    
    # sprite lists
    block_list = pygame.sprite.Group() # BOMBS ONLY
    explosion_list = pygame.sprite.Group() # EXPLOSIONS ONLY
    all_sprites_list = pygame.sprite.Group() # ALL SPRITES
    
    #adds both players to all_sprites_list
    all_sprites_list.add(player1)
    all_sprites_list.add(player2)

    # create sprite group and list that will be used to detect players' one-time collisions with explosions
    player1_possible_explosions = player1.differenceExplosions(explosion_list)
    hits1 = pygame.sprite.spritecollide(player1, player1_possible_explosions, False) # list of bombs that hit player
    player2_possible_explosions = player2.differenceExplosions(explosion_list)
    hits2 = pygame.sprite.spritecollide(player2, player2_possible_explosions, False) # list of bombs that hit player

    open = True # Boolean for if window is open
    game_start = False # Boolean for if game has been started
    
    # loads and scales to size background image for beginning
    beginning_bg = pygame.image.load("assets/firstpage3.png").convert()
    beginning_bg = pygame.transform.scale(beginning_bg, size)
    
    # loads and scales to size main game background
    midgame_bg = pygame.image.load("assets/bg3.png").convert()
    midgame_bg = pygame.transform.scale(midgame_bg, size)
    
    # loads and scales to size outer arena image
    outer_bg = pygame.image.load("assets/outer arena.png").convert_alpha() 
    outer_bg = pygame.transform.scale(outer_bg, size)
    
    # loads and scales to size end of the game background
    end_bg = pygame.image.load("assets/end2.png").convert()
    end_bg = pygame.transform.scale(end_bg, size)


    #loads music, sets volume to 0.5 and plays it on loop indefinitely
    pygame.mixer.music.load("assets/Simon_Bichbihler_In_the_1980s.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    # shows background
    screen.blit(beginning_bg, [0, 0])
    
    #creates the text
    write('Press SPACE to start',450,1360)
    write('Press CTRL to change',600,1360)
    write("the players' keys",700,1360)
    write("Press ESC to quit",850,1360)

    pygame.display.flip() # updates display window 
    
    while open:
    # main event loop
        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                open = False

            if event.type == pygame.KEYDOWN: # user presses a key
                if event.key == pygame.K_ESCAPE:
                    open = False
                
                if not(game_start):

                    if event.key == pygame.K_SPACE: # pressing space starts the game
                        game_start = True

                    if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL: # changing key settings on CTRL hit

                        for i in player1Keys: # browses each element in dictionary
                            next_key = False
                            screen.blit(beginning_bg, [0, 0]) # erases what was previously written
                            write('Changing keys for Player 1',475,1360)
                            write("Press key for: "+i.upper(),650,1360)
                            write('ESCAPE to skip a key',825,1360)
                            pygame.display.flip() # updates screen
                            while not(next_key): # while loop that stops when user presses desired key
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN: # user presses key
                                        if event.key != pygame.K_ESCAPE: # if user didn't press ESCAPE, key is changed.
                                            player1Keys[i]=event.key # corresponding key added to dictionnary
                                        next_key = True # ends while loop to start tests again for next key

                        for i in player2Keys: # same things for player 2
                            next_key = False
                            screen.blit(beginning_bg, [0, 0])
                            write('Changing keys for Player 2',475,1360)
                            write("Press key for: "+i.upper(),650,1360)
                            write('ESCAPE to skip a key',825,1360)
                            pygame.display.flip()
                            while not(next_key):
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key != pygame.K_ESCAPE:
                                            player2Keys[i]=event.key
                                        next_key = True
                        
                        screen.blit(beginning_bg, [0, 0])                
                        write('SPACE to play',600,1360)
                        write('ESC to quit',700,1360)
                        pygame.display.flip()
    
                else: # detect users pressing down on keys associated with movement
                    if event.key == player1Keys["up"]:
                        player1.up = True # player 1 is going up
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
                    if event.key == player1Keys["up"]: # detect users stopping movement
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
            pygame.time.delay(8)
            
            # calls tests from functions up top
            player1.move()
            player2.move()
            
            #loads background image
            screen.blit(midgame_bg, [0, 0])
            
            #updates player sprites
            player1.updateSpriteImage()
            player2.updateSpriteImage()
            
            # draws all the sprites
            all_sprites_list.draw(screen)
            
            # lowers player hp if they collide with an explosion
            player1_possible_explosions = player1.differenceExplosions(explosion_list)
            hits1 = pygame.sprite.spritecollide(player1, player1_possible_explosions, False) # list of bombs that hit player
            if hits1: # if the list is empty, it won't do anything
                player1.hp -= 20
                player1.addExplosionHits(hits1)
                
            player2_possible_explosions = player2.differenceExplosions(explosion_list)
            hits2 = pygame.sprite.spritecollide(player2, player2_possible_explosions, False) # list of bombs that hit player
            if hits2: # if the list is empty, it won't do anything
                player2.hp -= 20
                player2.addExplosionHits(hits2)

            Bombs.manageBomb(player1, block_list, player1.attack,  all_sprites_list, explosion_list, resized(250)) # Calling the function manageBomb in the file Bombs.py
            Bombs.manageBomb(player2, block_list, player2.attack,  all_sprites_list, explosion_list, resized(250)) # Calling the function manageBomb in the file Bombs.py
            
            #shows bg outside of arena to overlap possible explosions
            screen.blit(outer_bg, [0, 0])
            
            # update health bar. (self, hp, hpmax, xpos, ypos, longu, larg, c_vie, c_mort)
            life_bar1 = Barre_vie(player1.hp, hp_player1, resized(330), resized(110), resized(495), resized(75), (35, 145, 140), (4, 96, 104))
            life_bar2 = Barre_vie(player2.hp, hp_player2, resized(1105), resized(110), resized(495), resized(75), (186, 106, 202), (87, 42, 125))
            # shows health bars
            life_bar1.barres(screen)
            life_bar2.barres(screen)

            if player1.hp <= 0 or player2.hp <= 0:
                screen.blit(end_bg, [0, 0])
                
                # clears all lists to avoid collision detection after end
                block_list.empty()
                explosion_list.empty()
                all_sprites_list.empty()

                # determins which player won and writes it
                if player1.hp <= 0 and player2.hp <= 0:
                    write("It's a tie!",375,1450)
                elif player2.hp <= 0:
                    write('Player 1 won!',375,1450)
                else:
                    write("Player 2 won!",375,1450)
                
                # options at the end of the game
                # writing the options
                write("Press SPACE to try again", 625,1450)
                write("Press ESC to quit", 725,1450)
                # the actual options
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE: # pressing space starts the game
                            main()
                        elif event.key == pygame.K_ESCAPE: #pressing 'q' to quit the game
                            open = False
                    if event.type == pygame.QUIT:
                        open = False

            pygame.display.flip()

    # quits window once while loop is closed (open = False)  ## A MODIFIER
    pygame.quit()

if __name__ == '__main__': #avoid running main code when loaded as a module
    main()
