import pygame



# class Explosion(pygame.sprite.Sprite):
#     WHITE    = ( 255, 255, 255)
#     def __init__(self, colour, width, x, y):
#         radius = width/2
#         height = width
#         self.image = pygame.Surface([width, height])
#         pygame.draw.circle(self.image, colour, (x,y), radius)
#         # self.image.fill(colour)
#
#         # defines the size of the sprites
#         self.width = width
#         self.height = height
#
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y


class Bombs(pygame.sprite.Sprite):
    WHITE    = ( 255, 255, 255)
    def __init__(self, img, rect):

        #calls the class (Bombs) constructor, allows the sprite to initialise
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()  # updates the position of this object by setting the values of rect.x and rect.y
        self.timer = pygame.time.get_ticks()
        self.rect = self.rect.move(rect.x, rect.y-15)
        # print('bomb1')


    def explode(self):
        now = pygame.time.get_ticks()

        if now - self.timer > 3000 : # the delay is defined here
            # explosion = Explosion(WHITE, 70, self.rect.x, self.rect.y-15) # creates the circle of explosion (it replaces the bomb)
            # all_sprites_list.add(explosion)
            # block_list.add(explosion)
            self.kill()




def manageBomb (player, block_list, playerAttack, all_sprites_list):

    '''
    fonction qui prend comme argument player, block_list, playerAttack, all_sprites_list.

    Cette fonction est appelée dans la main loop "while open"

    Elle permet de
    - créer les bombes
    - aficher qqchose lorsqu'une bombe touche un joueur

    prochains objectifs
    - créer une zone de dégât
    - relier ce programme au barres de vie (un peu plus tard)

    '''

    hits = pygame.sprite.spritecollide(player, block_list, False) # list of bombs that hit player
    if hits: # if the list is empty, it won't do anything
        player.hit() # sera utilisé plus tard pour enlever des points de vie


    if playerAttack :
        if player.canPlaceBomb():
            bomb = Bombs('assets/bomb.png', player.rect) # creates the bomb for the player
            all_sprites_list.add(bomb)
            block_list.add(bomb)

    # for bomb in block_list :
    #     bomb.explode()


# if bomb2.colliderect(player1):
        # print('collision!')
        # player2.kill()
        # player1.kill()


