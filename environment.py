import pygame
import math
from base_entitiy import BaseEntity


class EnvironmentElement(BaseEntity):
    def __init__(self, pos, size, color, element_type, angle=0):
        super().__init__(pos, size, color)
        self.element_type = element_type
        self.angle = angle

    def update(self):
        pass

    def draw(self, screen):
        if self.element_type == "rectangle":
            rotated_surface = pygame.Surface(self.size, pygame.SRCALPHA)
            rotated_surface = pygame.transform.rotate(rotated_surface, math.degrees(self.angle))
            rotated_rect = rotated_surface.get_rect(center=(self.pos[0], self.pos[1]))
            pygame.draw.rect(screen, self.color, rotated_rect)
        elif self.element_type == "circle":
            pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size[0] // 2)
        elif self.element_type == "triangle":
            # Draw a triangle (adjust as needed)
            points = [(self.pos[0], self.pos[1] - self.size[1] // 2),
                      (self.pos[0] - self.size[0] // 2, self.pos[1] + self.size[1] // 2),
                      (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2)]
            pygame.draw.polygon(screen, self.color, points)
