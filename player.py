from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__()
        self.image = pygame.image.load() # add sprite image path here
        self.rect = self.image.get_frect(center=pos)