from settings import *
from player import Player
from level import Level
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # add game title here

        self.clock = pygame.time.Clock()
        self.running = True
        self.current_stage = Level()

        self.player = Player()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 # dt in ms
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
