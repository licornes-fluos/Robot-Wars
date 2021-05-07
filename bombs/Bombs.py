import pygame


class Explosion(pygame.sprite.Sprite):

    def __init__(self, colour, width, x, y):

        #calls the class (Bombs) constructor, allows the sprite to initialise
        super().__init__()

        PURPLE = (150, 131, 236)
        RANDOM = ( 220, 5, 50)

        radius = width/2
        height = width
        self.image = pygame.Surface([width, height])
        self.image.fill(RANDOM)
        self.image.set_colorkey(RANDOM)
        pygame.draw.circle(self.image, PURPLE, (width/2,width/2), radius)

        # defines position
        self.rect = self.image.get_rect()
        self.rect.x = x-radius
        self.rect.y = y-radius

        # this is to get the time when the the explosion circle is created
        self.timer = pygame.time.get_ticks()


    def exploded(self, all_sprites_list, block_list, explosion_list, size):
        """function that kills the explosion sprite after a delay"""

        now = pygame.time.get_ticks()

        if now - self.timer > 3000 : # the delay is defined here
            self.kill()

class Bombs(pygame.sprite.Sprite):

    PURPLE = (150, 131, 236)

    def __init__(self, img, rect):

        #calls the class (Bombs) constructor, allows the sprite to initialise
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()  # updates the position of this object by setting the values of rect.x and rect.y
        self.rect = self.rect.move(rect.x, rect.y-15)
        self.timer = pygame.time.get_ticks()
        self.bombsize = 50
        self.placement_adjust = self.bombsize/2


    def explode(self, all_sprites_list, block_list, explosion_list, size):
        now = pygame.time.get_ticks()
        if now - self.timer > 3000 : # the delay is defined here

            # creates the circle of explosion (it replaces the bomb)
            explosion = Explosion(Bombs.PURPLE, size, self.rect.x, self.rect.y-15)

            # creates the circle of explosion (it replaces the bomb)
            explosion = Explosion(Bombs.PURPLE, 250, self.rect.x, self.rect.y-15)
            all_sprites_list.add(explosion)
            explosion_list.add(explosion)
            self.kill()


            explosion = Explosion(Bombs.PURPLE, size, self.rect.x, self.rect.y-15) # creates the circle of explosion (it replaces the bomb)


            # print('bombed')

            explosion = Explosion(Bombs.PURPLE, 250, self.rect.x, self.rect.y-15) # creates the circle of explosion (it replaces the bomb)
            all_sprites_list.add(explosion)
            explosion_list.add(explosion)
            self.kill()


def manageBomb (player, block_list, playerAttack, all_sprites_list, explosion_list, size):

    '''
    fonction qui prend comme argument player, block_list, playerAttack, all_sprites_list.
    Cette fonction est appelée dans la main loop "while open"
    Elle permet de
    - créer les bombes
    - afficher qqchose lorsqu'une bombe touche un joueur
    '''

    # calls the explode function and applies it on the bomb sprites
    for bomb in block_list :
        bomb.explode(all_sprites_list, block_list, explosion_list, size)

    # calls the explosion function and applies it on the circles (damage zones)
    for explosion in explosion_list :
        explosion.exploded(all_sprites_list, block_list, explosion_list, size)

    if playerAttack :
        if player.canPlaceBomb():
            bomb = Bombs('assets/bomb.png', player.rect) # creates the bomb for the player
            all_sprites_list.add(bomb)
            block_list.add(bomb)
