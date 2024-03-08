import pygame
from base_entitiy import BaseEntity


# Character Class (Derived from BaseEntity)
class Character(BaseEntity):
    def __init__(self, pos, size, angle=0, hp=100, color=(0, 0, 255)):
        super().__init__(pos, size, color=color)
        self.angle = angle
        self.hp = hp

    def update(self):
        pass  # Implement specific logic for characters

    def draw(self, screen):
        adjusted_pos = (self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2)
        pygame.draw.rect(screen, self.color, pygame.Rect(adjusted_pos[0], adjusted_pos[1], self.size[0], self.size[1]))


# NPC Class (Derived from Character)
class NPC(Character):
    def __init__(self, pos, size, angle, hp, npc_type, color=(255, 0, 0)):
        super().__init__(pos, size, angle, hp, color=color)
        self.npc_type = npc_type

    def update(self):
        pass  # Implement specific logic for NPCs

# Player Class (Derived from Character)
class Player(Character):
    def __init__(self, pos, size, angle, hp, player_type, color=(0, 255, 0)):
        super().__init__(pos, size, angle, hp, color=color)
        self.player_type = player_type

    def update(self):
        pass  # Implement specific logic for players
