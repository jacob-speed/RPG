import pygame
import math
from base_entitiy import BaseEntity


# Character Class (Derived from BaseEntity)
class Character(BaseEntity):
    def __init__(self, pos, size, color, speed, angle=0, hp=100):
        super().__init__(pos, size, color)
        self.speed = speed
        self.angle = angle
        self.hp = hp

    def draw(self, screen):
        # Draw the character (equilateral triangle)
        rotated_points = [(x * math.cos(self.angle) - y * math.sin(self.angle) + self.pos[0],
                           x * math.sin(self.angle) + y * math.cos(self.angle) + self.pos[1])
                          for x, y in [(0, -self.size[1] // 2), (-self.size[0] // 2, self.size[1] // 2),
                                       (self.size[0] // 2, self.size[1] // 2)]]
        pygame.draw.polygon(screen, self.color, rotated_points)
