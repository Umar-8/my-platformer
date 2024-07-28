from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha() # make transparent background transparent
        self.rect = self.image.get_frect(center=pos)
        # movement
        self.direction = pygame.Vector2(0, 0)
        self.speed = 500

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        # normalizing for diagonal movement
        if self.direction:
            self.direction = self.direction.normalize()
        else:
            self.direction

    def update(self, dt):
        self.input()
        self.move(dt)