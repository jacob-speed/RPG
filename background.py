import pygame
import math
from base_entitiy import BaseEntity


class Background(BaseEntity):
    def __init__(self, pos, size, color, texture):
        super().__init__(pos, size, color)
        self.element_type = texture

    def draw(self, screen):
        x_pos, y_pos = 100, 100
        x_needed = self.size[0] // x_pos + 1
        y_needed = self.size[0] // y_pos + 1
        rect_needed = max(x_needed, y_needed)
        for i in range(-3, rect_needed):
            x_pos_new = (self.pos[0] + x_pos * i) % (self.size[0] + 100) - 50
            y_pos_new = (self.pos[1] + y_pos * i) % (self.size[1] + 100) - 50
            pygame.draw.rect(screen, self.color, self.get_rect_x(x_pos_new))
            pygame.draw.rect(screen, self.color, self.get_rect_y(y_pos_new))

    def get_rect_x(self, new_x):
        pos = (new_x, 0)
        size = (50, self.size[1])
        return pos, size

    def get_rect_y(self, new_y):
        pos = (0, new_y)
        size = (self.size[0], 50)
        return pos, size
