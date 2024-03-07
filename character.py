import pygame
import math

class Character:
    def __init__(self, screen_width, screen_height):
        self.size = 50
        self.angle = 0
        self.pos = [screen_width // 2, screen_height // 2]
        self.speed = 5

    def rotate(self, mouse_x, mouse_y):
        self.angle = math.atan2(mouse_y - self.pos[1], mouse_x - self.pos[0]) + math.pi / 2

    def move(self, keys):
        if keys[pygame.K_w]:
            self.pos[1] -= self.speed
        if keys[pygame.K_s]:
            self.pos[1] += self.speed
        if keys[pygame.K_a]:
            self.pos[0] -= self.speed
        if keys[pygame.K_d]:
            self.pos[0] += self.speed

    def get_projectile_start_pos(self):
        # Adjust the starting position based on the character's direction
        x = self.pos[0] + self.size * math.cos(self.angle)
        y = self.pos[1] + self.size * math.sin(self.angle)
        return x, y
