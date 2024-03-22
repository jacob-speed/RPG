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
        self.hit = False


    def draw(self, screen):
        # Draw the character (equilateral triangle)
        rotated_points = [(x * math.cos(self.angle) - y * math.sin(self.angle) + self.pos[0],
                           x * math.sin(self.angle) + y * math.cos(self.angle) + self.pos[1])
                          for x, y in [(0, -self.size[1] // 2), (-self.size[0] // 2, self.size[1] // 2),
                                       (self.size[0] // 2, self.size[1] // 2)]]
        pygame.draw.polygon(screen, self.color, rotated_points)
        # Render HP text
        font = pygame.font.Font(None, 36)  # You can change the font and size as needed
        hp_text = font.render(f"{self.hp}", True, (255, 0, 0))  # White color
        text_rect = hp_text.get_rect(center=(self.pos[0], self.pos[1] - 50))  # Position text in the center of the character
        screen.blit(hp_text, text_rect)

    def is_hit(self, damage):
        self.hp -= damage
        self.hit = True

    def next_skill(self):
        if len(self.skills) == 0:
            pass
        else:
            self.selected_skill = (self.selected_skill + 1) % len(self.skills)

    def previous_skill(self):
        if len(self.skills) > 0:
            self.selected_skill = (self.selected_skill - 1) % len(self.skills)

    def select_skill(self, skill_num):
        if len(self.skills) > 0:
            self.selected_skill = skill_num - 1

    def use_skill(self):
        if len(self.skills) > 0:
            angle = self.angle_to_point(pygame.mouse.get_pos()) - math.pi/2
            pos = (self.pos[0] + math.cos(angle) * 45, self.pos[1] + math.sin(angle) * 45)
            return self.skills[self.selected_skill].use(pos, angle)

