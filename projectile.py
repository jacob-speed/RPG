import pygame
import math

class Projectile:
    def __init__(self, start_pos, angle, speed):
        self.pos = list(start_pos)
        self.angle = angle - math.pi/2
        self.speed = speed

    def move(self):
        self.pos[0] += self.speed * math.cos(self.angle)
        self.pos[1] += self.speed * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos[0]), int(self.pos[1])), 5)
