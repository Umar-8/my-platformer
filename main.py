from settings import *
from player import Player
from pytmx.util_pygame import load_pygame
from sprites import *
from groups import AllSprites
class Game:
    def __init__(self) -> None:
        # initializing game
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # add game title here
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = AllSprites()
        self.collisions_sprites = pygame.sprite.Group()

        self.setup()


    def setup(self):
        map = load_pygame(join('tmx', 'myworld.tmx'))
        for x, y, image in map.get_layer_by_name('Tile Layer 1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collisions_sprites))

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collisions_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collisions_sprites)
                self.gun = Gun(self.player, self.all_sprites)



    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 # dt in ms
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.all_sprites.update(dt)

            # prevent last frames from getting seen
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
