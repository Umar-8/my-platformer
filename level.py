from settings import *

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface() # gives us display surface created in main

    def run(self):
        self.display_surface.fill('purple')