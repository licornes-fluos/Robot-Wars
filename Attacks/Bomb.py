# Defining some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)



player1Attack = bool()
player2Attack = bool()

class Bombs(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):

        #calls the class (Bombs) constructor, allows the sprite to initialise
        super().__init__()

        # creates an image of the block
        # fills it with a colour.
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # updates the position of this object by setting the values of rect.x and rect.y
        # self.rect = self.image.get_rect()

    # def __init__(self,x,y):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.image.load('Enemy.gif').convert()
    #     self.rect = self.image.get_rect(x=x, y=y)

    # def delay:
        # running = 1
        # counter = 0
        # while running:
            # pygame.time.delay(10)

    # counter += 1
        # if counter >= 200:
            # enemyship_sprites.add(Enemy(320))
        # counter = 0

    def exploded(self):
        for enemy in all_sprites_list:
            if enemy.rect.x<100:
                 all_sprites_list(enemy)


    def is_collided_with(self, sprite):
    return self.rect.colliderect(sprite.rect)
    # colliderect() is a test to see if two rectangles overlap. It returns true if any portion of either rectangle overlap (except the top+bottom or left+right edges)).





--------------------------------------------------------------

while open:
    # main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            open = False
            print("Quit")

        if event.type == pygame.KEYDOWN: # user presses a key
            if start:
                if event.key == player1Keys["attack"]:
                    player1Attack = True
                if event.key == player2Keys["attack"]:
                    player2Attack = True

        elif event.type == pygame.KEYUP: # user stops pressing a key
            if start:

                if event.key == player1Keys["attack"]:
                    player1Attack = False
                if event.key == player2Keys["attack"]:
                    player2Attack = False


    # --- Game logic

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

--------------------------------------------------------------





