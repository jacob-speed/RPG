import pygame
import math
from base_entitiy import BaseEntity


# Projectile Class (Derived from BaseEntity)
class Projectile(BaseEntity):
    def __init__(self, pos, size, color, angle, speed):
        super().__init__(pos, size, color)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.pos[0] += self.speed * math.cos(self.angle)
        self.pos[1] += self.speed * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size[0] // 2)

    def is_beyond_screen(self, width, length):
        is_within_screen = -100 <= self.pos[0] <= width + 100 and -100 <= self.pos[1] <= length + 100
        return not is_within_screen


