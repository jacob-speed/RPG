import pygame
from character import Character


# Player Class (Derived from Character)
class Player(Character):
    def __init__(self, pos, size, color, speed, angle, hp):
        super().__init__(pos, size, color, speed, angle, hp)

    def rotate(self, mouse_x, mouse_y):
        self.angle = self.angle_to_point((mouse_x, mouse_y))

    def update_position(self, keys, speed, move):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rotate(mouse_x, mouse_y)
