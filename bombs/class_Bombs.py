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