import pygame


# BaseEntity Class
class BaseEntity:
    def __init__(self, pos, size, color):
        position = list(pos)
        self.pos = list(pos)
        self.size = size
        self.color = color

    def move(self, keys, player_speed):
        if keys[pygame.K_w]:
            self.pos[1] += player_speed
        if keys[pygame.K_s]:
            self.pos[1] -= player_speed
        if keys[pygame.K_a]:
            self.pos[0] += player_speed
        if keys[pygame.K_d]:
            self.pos[0] -= player_speed

    def update(self):
        pass

    def draw(self, screen):
        pass
