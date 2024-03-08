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

#TODO need to delete projectiles once they are significantly off the screen

