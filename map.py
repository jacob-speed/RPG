import pygame
import os
import random
from environment import EnvironmentElement
from npc import NPC


class Map:
    def __init__(self, pos, scale):
        self.pos = pos
        self.scale = scale
        self.environment_elements = []
        self.mob = []

    def load_tile(self, fileid):
        file_path = os.path.join("tiles", f"tile{fileid}.png")
        tile_image = pygame.image.load(file_path)
        previous_element = False
        for x in range(0, tile_image.get_width()):
            for y in range(0, tile_image.get_height()):
                if tile_image.get_at((x, y)) == (0, 0, 0, 255):
                    if previous_element:
                        prev_size = self.environment_elements[-1].size
                        self.environment_elements[-1].set_size((prev_size[0], prev_size[1] + self.scale))
                        elem = self.environment_elements[-1]
                        print(elem.pos, elem.size)
                    else:
                        pos = (x * self.scale + self.pos[0], y * self.scale + self.pos[1])
                        ele = EnvironmentElement(pos, (self.scale, self.scale), (0, 0, 0), "rectangle")
                        print(ele.pos, ele.size)
                        self.environment_elements.append(ele)
                        previous_element = True
                else:
                    previous_element = False
                if tile_image.get_at((x, y)) == (255, 0, 0, 255):
                    self.generate_mob((x, y))
            previous_element = False


    def generate_mob(self, pos):
        mob_size = random.randint(3, 5)
        for i in range(0, mob_size):
            pos_x = self.pos[0] + pos[0] * self.scale + random.randint(-self.scale // 3, self.scale // 3)
            pos_y = self.pos[1] + pos[1] * self.scale + random.randint(-self.scale // 3, self.scale // 3)
            new_npc = NPC((pos_x, pos_y), (60, 60), (255, 0, 0))
            self.mob.append(new_npc)
