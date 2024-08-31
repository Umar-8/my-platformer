from settings import *
from player import Player
from pytmx.util_pygame import load_pygame
from sprites import *
from groups import AllSprites
from random import choice

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
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


        # timer
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 100

        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 800)
        self.spawn_positions = []

        self.load_images()
        self.setup()

    def load_images(self):
        self.bullet_surf = pygame.image.load(join('images', 'weapons', 'bullet', 'bullet.png')).convert_alpha()

        folder = walk(join('images', 'enemies', 'bat'))
        self.enemy_frames = []
        for path, folders, file_names in folder:
            if file_names:
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames.append(surf)


    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.gun.rect.center + (self.gun.player_direction * 50)
            Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

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
            # adding enemy markers positions from tiled
            else:
                self.spawn_positions.append((obj.x, obj.y))


    def gun_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True

    def bullet_collision(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                collision_sprites = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False, pygame.sprite.collide_mask)
                if collision_sprites:
                    for sprite in collision_sprites:
                        sprite.destroy()
                    bullet.kill()

    def player_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask):
            self.running = False


    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 # dt in ms
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.enemy_event:
                    Enemy(choice(self.spawn_positions), self.enemy_frames, (self.all_sprites, self.enemy_sprites), self.player, self.collisions_sprites)

            self.all_sprites.update(dt)

            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            self.player_collision()

            # prevent last frames from getting seen
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()


        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
