import pygame
import math
from base_entitiy import BaseEntity


class EnvironmentElement(BaseEntity):
    def __init__(self, pos, size, color, element_type, angle=0):
        super().__init__(pos, size, color)
        self.element_type = element_type
        self.angle = angle

    def draw(self, screen):
        if self.element_type == "rectangle":
            pygame.draw.rect(screen, self.color, ((self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2), self.size))
            # rotated_points = [
            #     (self.pos[0] + math.cos(self.angle) * (x - self.pos[0]) - math.sin(self.angle) * (y - self.pos[1]),
            #      self.pos[1] + math.sin(self.angle) * (x - self.pos[0]) + math.cos(self.angle) * (y - self.pos[1]))
            #     for x, y in [(self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2),
            #                  (self.pos[0] + self.size[0] / 2, self.pos[1] - self.size[1] / 2),
            #                  (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2),
            #                  (self.pos[0] - self.size[0] / 2, self.pos[1] + self.size[1] / 2)]
            # ]
            # pygame.draw.polygon(screen, self.color, rotated_points)
        elif self.element_type == "circle":
            pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size[0] // 2)
        elif self.element_type == "triangle":
            # Draw a rotated triangle
            rotated_points = [
                (self.pos[0] + math.cos(self.angle) * (x - self.pos[0]) - math.sin(self.angle) * (y - self.pos[1]),
                 self.pos[1] + math.sin(self.angle) * (x - self.pos[0]) + math.cos(self.angle) * (y - self.pos[1]))
                for x, y in [(self.pos[0], self.pos[1] - self.size[1] // 2),
                             (self.pos[0] - self.size[0] // 2, self.pos[1] + self.size[1] // 2),
                             (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2)]
            ]
            pygame.draw.polygon(screen, self.color, rotated_points)

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_size(self, new_size):
        self.size = new_size
