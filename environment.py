import pygame
import math
from base_entitiy import BaseEntity


# EnvironmentElement Class (Derived from BaseEntity)
class EnvironmentElement(BaseEntity):
    def __init__(self, pos, size, element_type, angle=0):
        super().__init__(pos, size)
        self.element_type = element_type
        self.angle = angle

    def update(self):
        pass  # Implement specific logic for environment elements

    def draw(self, screen):
        if self.element_type == "rectangle":
            rotated_surface = pygame.Surface(self.size, pygame.SRCALPHA)
            rotated_surface = pygame.transform.rotate(rotated_surface, math.degrees(self.angle))
            rotated_rect = rotated_surface.get_rect(center=(self.pos[0], self.pos[1]))
            pygame.draw.rect(screen, (0, 0, 0), rotated_rect)
        elif self.element_type == "circle":
            pygame.draw.circle(screen, (0, 0, 0), (int(self.pos[0]), int(self.pos[1])), self.size[0] // 2)
        elif self.element_type == "triangle":
            # Draw a triangle (adjust as needed)
            points = [(self.pos[0], self.pos[1] - self.size[1] // 2),
                      (self.pos[0] - self.size[0] // 2, self.pos[1] + self.size[1] // 2),
                      (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2)]
            pygame.draw.polygon(screen, (0, 0, 0), points)


# Projectile Class (Derived from BaseEntity)
class Projectile(BaseEntity):
    def __init__(self, pos, size, angle, speed):
        super().__init__(pos, size, speed)
        self.angle = angle

    def update(self):
        self.pos[0] += self.speed * math.cos(self.angle)
        self.pos[1] += self.speed * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos[0]), int(self.pos[1])), self.size[0] // 2)
