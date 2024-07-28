from settings import *
from player import Player
from pytmx.util_pygame import load_pygame

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

        # sprites
        self.player = Player((400, 300), self.all_sprites)

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
