from settings import *
from player import Player
from pytmx.util_pygame import load_pygame
from sprites import *
from random import randint

class Game:
    def __init__(self) -> None:
        # initializing game
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # add game title here
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collisions_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((400, 300), self.all_sprites, self.collisions_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(20, 60), randint(40,80)
            CollisionSprite((x, y), (w, h), (self.all_sprites, self.collisions_sprites))

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 # dt in ms
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.all_sprites.update(dt)

            # prevent last frames from getting seen
            self.display_surface.fill("black")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
