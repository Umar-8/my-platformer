from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)

class Gun(pygame.sprite.Sprite):
    def init(self, player, groups):
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(1, 0)

        super().__init__(groups)
        self.gun_surf = pygame.image.load(join('images', 'weapons', 'gun', 'golden_friend.png')).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_direction * self.distance)

