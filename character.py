import pygame
import math
from base_entitiy import BaseEntity


# Character Class (Derived from BaseEntity)
class Character(BaseEntity):
    def __init__(self, pos, size, color, speed, skills=None, angle=0, hp=100):
        super().__init__(pos, size, color)
        self.speed = speed
        self.angle = angle
        self.hp = hp
        if skills is None:
            self.skills = []
        else:
            self.skills = skills
        self.selected_skill = 0


    def draw(self, screen):
        # Draw the character (equilateral triangle)
        rotated_points = [(x * math.cos(self.angle) - y * math.sin(self.angle) + self.pos[0],
                           x * math.sin(self.angle) + y * math.cos(self.angle) + self.pos[1])
                          for x, y in [(0, -self.size[1] // 2), (-self.size[0] // 2, self.size[1] // 2),
                                       (self.size[0] // 2, self.size[1] // 2)]]
        pygame.draw.polygon(screen, self.color, rotated_points)

    def next_skill(self):
        if len(self.skills) == 0:
            pass
        else:
            self.selected_skill = (self.selected_skill + 1) % len(self.skills)

    def previous_skill(self):
        if len(self.skills) == 0:
            pass
        else:
            self.selected_skill = (self.selected_skill - 1) % len(self.skills)

    def use_skill(self):
        if len(self.skills) == 0:
            pass
        else:
            angle = self.angle_to_point(pygame.mouse.get_pos()) - math.pi/2
            pos = (self.pos[0] + math.cos(angle) * 45, self.pos[1] + math.sin(angle) * 45)
            return self.skills[self.selected_skill].use(pos, angle)

