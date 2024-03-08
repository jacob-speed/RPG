import pygame
import math
from base_entitiy import BaseEntity


# Character Class (Derived from BaseEntity)
class Character(BaseEntity):
    def __init__(self, pos, size, color, speed, angle=0, hp=100, ):
        super().__init__(pos, size, color)
        self.speed = speed
        self.angle = angle
        self.hp = hp

    def update(self):
        pass  # Implement specific logic for characters

    def draw(self, screen):
        # Draw the character (equilateral triangle)
        rotated_points = [(x * math.cos(self.angle) - y * math.sin(self.angle) + self.pos[0],
                           x * math.sin(self.angle) + y * math.cos(self.angle) + self.pos[1])
                          for x, y in [(0, -self.size[1] // 2), (-self.size[0] // 2, self.size[1] // 2),
                                       (self.size[0] // 2, self.size[1] // 2)]]
        pygame.draw.polygon(screen, self.color, rotated_points)


# NPC Class (Derived from Character)
class NPC(Character):
    def __init__(self, pos, size, color, speed, angle, hp, npc_type):
        super().__init__(pos, size, color, speed, angle, hp)
        self.npc_type = npc_type

    def update(self):
        pass  # Implement specific logic for NPCs

# Player Class (Derived from Character)
class Player(Character):
    def __init__(self, pos, size, color, speed, angle, hp):
        super().__init__(pos, size, color, speed, angle, hp)

    def rotate(self, mouse_x, mouse_y):
        self.angle = math.atan2(mouse_y - self.pos[1], mouse_x - self.pos[0]) + math.pi / 2

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rotate(mouse_x, mouse_y)

    def move(self, keys, speed, move):
        # Player is always centred. Overload move method so that player doesn't move.
        pass
