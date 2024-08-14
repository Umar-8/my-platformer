from typing import Iterable
from pygame.sprite import AbstractGroup
from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, target_position):
        self.offset.x = -(target_position[0] - WINDOW_WIDTH / 2) # middle of the screen
        self.offset.y = -(target_position[1] - WINDOW_HEIGHT / 2) # middle of the screen (vertical)

        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)