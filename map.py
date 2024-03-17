import pygame
import os
from environment import EnvironmentElement


class Map():
    def __init__(self, pos):
        self.pos = pos
        self.environment_elements = []

    def load_tile(self, id):
        file_path = os.path.join("tiles", f"tile{id}.png")
        tile_image = pygame.image.load(file_path)
        for x in range(0, tile_image.get_width()):
            for y in range(0, tile_image.get_height()):
                if tile_image.get_at((x, y)) == (0, 0, 0, 255):
                    pos = (x * 400 + self.pos[0], y * 400 + self.pos[1])
                    ele = EnvironmentElement(pos, (500, 500), (0, 0, 0), "rectangle")
                    self.environment_elements.append(ele)
        for ele in self.environment_elements:
            print(ele.pos)
