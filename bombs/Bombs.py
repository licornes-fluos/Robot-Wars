
    while open:
    # main event loop
        for event in pygame.event.get(): # User did something

            if event.type == pygame.KEYDOWN: # user presses a key
                if not(game_start):
                    if game_start:

                        if event.key == player1Keys["attack"]:
                            player1Attack = True
                        if event.key == player2Keys["attack"]:
                            player2Attack = True

            elif event.type == pygame.KEYUP: # user stops pressing a key
                if game_start:

                    if event.key == player1Keys["attack"]:
                        player1Attack = False
                    if event.key == player2Keys["attack"]:
                        player2Attack = False




        hits1 = pygame.sprite.spritecollide(player1, block_list, False) # list of bombs that hit player 1
        if hits1: # if the list is empty, it won't do anything
            print('Player1Hit!')


        hits2 = pygame.sprite.spritecollide(player2, block_list, False) # list of any sprite from block_list that hit player2
        if hits2:
            print('Player2Hit!')


        canPlaceBomb1 = True
        canPlaceBomb2 = True

        if player2Attack :
            print('bomb2')
            if canPlaceBomb2 == True :
                # get_rawtime() # in milliseconds
                bomb2 = Bombs(BLACK, 20, 20) # creates the bomb for the player
                bomb2.rect.x = player2.rect.x + 5 # Affiche la bombe aux coordonnées du joueur
                bomb2.rect.y = player2.rect.y + 5 # le "+5" c'est juste pour centrer la bombe
                block_list.add(bomb2)
                all_sprites_list.add(bomb2)

        # if bomb2.colliderect(player1):
            # print('collision!')
            # player2.kill()
            # player1.kill()


        if player1Attack :
            print('bomb1')
            if canPlaceBomb1 == True :
                # get_rawtime() # in milliseconds
                bomb1 = Bombs(BLACK, 20, 20) # creates the bomb for the player
                bomb1.rect.x = player1.rect.x + 5 # Affiche la bombe aux coordonnées du joueur
                bomb1.rect.y = player1.rect.y + 5 # le "+5" c'est juste pour centrer la bombe
                block_list.add(bomb1)
                all_sprites_list.add(bomb1)

        # if bomb2.colliderect(player1):
            # print('collision!')
            # player2.kill()
            # player1.kill()
